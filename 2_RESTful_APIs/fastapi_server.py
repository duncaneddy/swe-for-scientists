"""
Simple example FastAPI server
"""

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

@app.get("/")
def hello():
    return {"Hello": "World"}

class Person(BaseModel):
    name: str

@app.post("/hello")
def hello_post(person: Person):
    return {"Hello": person.name}