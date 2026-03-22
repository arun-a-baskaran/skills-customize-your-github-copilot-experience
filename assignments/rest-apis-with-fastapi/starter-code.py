# Starter Code for REST APIs with FastAPI Assignment

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel


app = FastAPI()


class Item(BaseModel):
    id: int
    name: str
    completed: bool


items = [
    {"id": 1, "name": "Finish FastAPI homework", "completed": False},
    {"id": 2, "name": "Review API responses", "completed": True},
]


@app.get("/")
def read_root():
    return {"message": "Welcome to the FastAPI assignment"}


# Task 1:
# Review the FastAPI app, Item model, and sample data above.


# Task 2:
# Add a GET /items route that returns all items.


# Task 2:
# Add a POST /items route that accepts an Item and appends it to the items list.


# Task 2:
# Add a PUT /items/{item_id} route that updates the completed status.
# If the item is not found, raise an HTTPException with status code 404.