from fastapi import FastAPI

app = FastAPI()

@app.get("/order-burger")
def order_burger(item: str = "Cheeseburger"):
    return {"status": "success", "order": item, "eta": "15 minutes"}

@app.get("/book-flight")
def book_flight(destination: str = "New York"):
    return {"status": "success", "flight": destination, "price": "$250"}

@app.get("/get-insurance")
def get_insurance(plan: str = "Basic Health"):
    return {"status": "success", "plan": plan, "premium": "$100/month"}
