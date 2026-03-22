# 📘 Assignment: REST APIs with FastAPI

## 🎯 Objective

Build a simple REST API using the FastAPI framework. In this assignment, students will practice creating API routes, working with request and response data, and returning JSON from a Python web application.

## 📝 Tasks

### 🛠️	Create the FastAPI Application

#### Description
Use the starter code to set up a FastAPI app and define the data model for a small item-tracking API.

#### Requirements
Completed program should:

- Create a FastAPI application object.
- Define a Pydantic model for an item with at least an `id`, `name`, and `completed` field.
- Store items in a simple in-memory list.
- Add a root route such as `/` that returns a short welcome message in JSON format.


### 🛠️	Build REST API Endpoints

#### Description
Implement API routes that allow a user to view, add, and update items in the item-tracking API.

#### Requirements
Completed program should:

- Add a `GET /items` route that returns all items.
- Add a `POST /items` route that accepts item data and adds a new item.
- Add a `PUT /items/{item_id}` route that updates the `completed` status of an existing item.
- Return clear JSON responses for successful requests.
- Return an appropriate error response if the requested item does not exist.

```json
{
  "message": "Welcome to the FastAPI assignment"
}
```