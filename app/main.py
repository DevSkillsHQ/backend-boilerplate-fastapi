from typing import Optional

from fastapi import FastAPI

app = FastAPI()


@app.get("/ping")
def read_root():
    return {"response": "pong"}