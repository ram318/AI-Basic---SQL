import ollama
from fastapi import FastAPI
import sqlite3
import re

app = FastAPI()

# Function to generate SQL using Ollama
def generate_sql(query):
    system_prompt = "You are an AI that converts English questions into SQL queries. The table name is 'students' with columns: name, rollno, mathsmarks, sciencemarks, socialmarks. Respond ONLY with the SQL query, without any explanations or markdown formatting."
    
    response = ollama.chat(
        model="codellama",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": query}
        ]
    )
    
    # Extract only the SQL part (remove any extra text)
    sql_query = response["message"]["content"].strip()
    sql_query = re.sub(r'```sql|```', '', sql_query)  # Remove markdown formatting if present
    return sql_query

# Function to execute SQL on SQLite
def execute_sql(query):
    connection = sqlite3.connect("students.db")
    cursor = connection.cursor()
    
    cursor.execute(query)
    result = cursor.fetchall()
    
    connection.close()
    return result

# FastAPI endpoint to process user queries
@app.get("/query/")
def process_query(question: str):
    sql_query = generate_sql(question)
    result = execute_sql(sql_query)
    
    return {"query": sql_query, "result": result}
