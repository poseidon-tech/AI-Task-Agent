# AI Task Agent

An **AI-powered task automation chatbot** that connects natural language requests to real backend APIs.  
Ask it things like:

- “Buy me a burger” 🍔 → triggers a food ordering API  
- “Book a flight to New York” ✈️ → connects with a flight booking API  
- “Get me an insurance quote” 🛡️ → integrates with an insurance API  

The agent uses **LLMs (Large Language Models)**, intent recognition, and a pluggable backend API system to execute real-world tasks from plain text input.

---

## 🚀 Features

- **Natural Language → API Call**: Converts user intent into backend function execution.
- **Prompt Tuning**: Optimized prompts to improve accuracy and reduce ambiguity.
- **Streaming Responses**: Supports real-time streaming replies for interactive conversations.
- **Modular Backend Connectors**: Easily extendable for new APIs (food, travel, insurance, etc.).
- **Rapid A/B Testing**: Test different model prompts and workflows quickly.
- **Production-ready MCP Agent Core**: Built on top of MCP-Agent for scalability.

---

## 🛠️ Tech Stack

- **Python 3.10+**
- **LLM Support**: OpenAI GPT / local models
- **Framework**: MCP-Agent
- **Vector Search**: FAISS / ChromaDB (optional for retrieval tasks)
- **Infra-as-Code Ready**
- **Version Control**: Git + GitHub

---

## 📂 Project Structure

ai-task-agent/
│── src/ # Core agent code
│── examples/ # Example chatbot demos
│ └── task_agent_demo # Main demo (burger, flight, insurance booking)
│── workflows/ # Predefined workflows
│── tests/ # Unit tests
│── README.md # This file
│── requirements.txt # Python dependencies

yaml
Copy
Edit

---

## ▶️ Quick Start

  Clone the repo  
   ```bash
   git clone https://github.com/poseidon-tech/AI-Task-Agent.git
   cd AI-Task-Agent

  Install dependencies

  pip install -r requirements.txt
  Set your OpenAI API key (or any other LLM provider):
  export OPENAI_API_KEY=your_key_here


  Run the demo chatbot:

  python examples/task_agent_demo/main.py
  📖 Example Usage

  > User: Book me a flight to San Francisco tomorrow
  > Agent: ✅ Flight booking request sent via FlightAPI

  > User: I want to buy a cheeseburger combo
  > Agent: 🍔 Order placed successfully with BurgerAPI

  > User: Get me health insurance options
  > Agent: 🛡️ Pulled top insurance quotes from InsuranceAPI