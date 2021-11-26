from typing import Optional

from fastapi import FastAPI

from databases import Database

database = Database("sqlite:///app.db")

app = FastAPI()

# NOTE: Feel free to restructure the code and database schema the way you prefer. This is only an example.

@app.on_event("startup")
async def database_connect():
    await database.connect()
    query = """CREATE TABLE IF NOT EXISTS HighScores (id INTEGER PRIMARY KEY, name VARCHAR(100), score INTEGER)"""
    await database.execute(query=query)

    query = "INSERT INTO HighScores(name, score) VALUES (:name, :score)"
    values = [
        {"name": "Daisy", "score": 92},
        {"name": "Neil", "score": 87},
        {"name": "Carol", "score": 43},
    ]
    await database.execute_many(query=query, values=values)


@app.on_event("shutdown")
async def database_disconnect():
    await database.disconnect()


@app.get("/ping")
async def ping():
    query = "SELECT name,score FROM HighScores"
    rows = await database.fetch_all(query=query)
    return {"rows": rows}
