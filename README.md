# 📊 statista_demo

#### A FastAPI demo project simulating a simplified version of the Statista API, with semantic search and streaming support.

## 🚀 Features

- `GET /find` — Returns the top-5 most relevant results for a natural language query.
- `GET /stream/find` — Streams the top-10 results progressively using HTTP streaming.
- `GET /data` — Returns all available mock data (100 records).

## 🛠️ Setup & Run (Docker + Makefile)

> Make sure you have **Docker** and **Make** installed.

### 🔧 Build and run the service

```bash
make up-build
```

### 📬 Example usage
#### Test the endpoints using Postman, curl, or your browser:

http://localhost:8000/find?query=latest+technology

http://localhost:8000/stream/find?query=renewable+energy

http://localhost:8000/data


### 🧠 Notes
#### This is a simplified prototype. For large-scale or production use, additional considerations would be required (scaling, observability, authentication, etc).

### You can use generated data (not from JSON file) by doing two steps:
#### 1) uncomment line number 5 in main.py file
#### 2) comment out lines 13 through 16

#### in this case the data will be generated using faker library, but it will be less meaningful