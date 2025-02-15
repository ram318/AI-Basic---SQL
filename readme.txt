# Query System with Ollama and FastAPI

## Overview
This project provides a natural language query system that converts user questions into SQL queries using **Codellama (via Ollama)** and executes them on an SQLite database. It includes:
- `setup_db.py`: Initializes the database.
- `main.py`: Handles API requests and integrates with Ollama.

## Prerequisites
Before running this project, ensure you have the following installed:
- Python 3.8+
- SQLite
- Ollama (for running Codellama)

## Setup Steps

### Step 1: Create a Virtual Environment (Optional but Recommended)
```sh
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```
**Why?** This keeps dependencies isolated.

### Step 2: Install Dependencies
```sh
pip install fastapi uvicorn sqlite3 ollama
```
**Why?** These are required for API handling, database access, and LLM integration.

### Step 3: Install Ollama
Follow [Ollama's installation guide](https://ollama.com) for your OS.
```sh
ollama pull codellama
```
**Why?** Ollama runs Codellama, which converts English queries into SQL.

### Step 4: Set Up the Database
```sh
python setup_db.py
```
**Why?** This script creates the `students` table and populates it with sample data.

### Step 5: Start the FastAPI Server
```sh
uvicorn main:app --reload
```
**Why?** This starts the API, allowing you to send queries.

### Step 6: Test the API
Send a request using a browser or `curl`:
```sh
curl "http://127.0.0.1:8000/query/?question=How many students scored more than 60 in maths?"
```
Or use Python:
```python
import requests
response = requests.get("http://127.0.0.1:8000/query/", params={"question": "How many students scored more than 60 in maths?"})
print(response.json())
```

## Stopping the Server
Press **Ctrl+C** in the terminal.

## Troubleshooting
- **Ollama not running?** Start it with:
  ```sh
  ollama run codellama
  ```
- **Syntax errors in SQL?** Ensure Ollama returns clean SQL using `generate_sql()` in `main.py`.
- **FastAPI not recognized?** Activate the virtual environment and reinstall dependencies.

---
Now, your natural language query system is ready! 🚀

