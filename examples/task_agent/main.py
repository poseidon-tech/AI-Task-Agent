import asyncio
import requests
from mcp_agent.app import MCPApp
from mcp_agent.agents.agent import Agent
from mcp_agent.workflows.llm.augmented_llm_openai import OpenAIAugmentedLLM

# Your app definition
app = MCPApp(name="task_agent_demo")

# Mock API endpoints (from mock_apis.py)
BURGER_API = "http://localhost:8000/order-burger"
FLIGHT_API = "http://localhost:8000/book-flight"
INSURANCE_API = "http://localhost:8000/get-insurance"


async def run_demo():
    async with app.run() as mcp_agent_app:
        logger = mcp_agent_app.logger

        # Define the agent with instructions
        task_agent = Agent(
            name="task_agent",
            instruction="""You are an assistant that helps users complete tasks.
            Classify user requests into one of these categories:
            - order_food (burger)
            - book_flight
            - get_insurance
            Then call the right API to fulfill it.""",
        )

        async with task_agent:
            # Attach an OpenAI LLM (default GPT-4o)
            llm = await task_agent.attach_llm(OpenAIAugmentedLLM)

            print("🤖 AI Task Agent Ready! Type 'exit' to quit.")
            while True:
                user_input = input("\nUser: ")
                if user_input.lower() in ["exit", "quit"]:
                    break

                # Use the LLM to classify the intent
                intent = await llm.generate_str(
                    f"Classify this request: '{user_input}' "
                    "into [order_food, book_flight, get_insurance]. "
                    "Return only the label."
                )
                intent = intent.strip().lower()
                logger.info(f"Predicted intent: {intent}")

                # Route to the correct API
                if "order" in intent or "food" in intent or "burger" in intent:
                    response = requests.get(BURGER_API, params={"item": "Cheeseburger"})
                elif "flight" in intent:
                    response = requests.get(FLIGHT_API, params={"destination": "New York"})
                elif "insurance" in intent:
                    response = requests.get(INSURANCE_API, params={"plan": "Basic Health"})
                else:
                    print("🤖 Sorry, I couldn't understand that request.")
                    continue

                print("🤖 Response:", response.json())


if __name__ == "__main__":
    asyncio.run(run_demo())
