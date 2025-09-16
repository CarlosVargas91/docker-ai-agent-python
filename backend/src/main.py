import os
from fastapi import FastAPI

app = FastAPI()

MY_PROJECT = os.getenv("MY_PROJECT")
API_KEY = os.getenv("API_KEY")

if not API_KEY:
    raise NotImplementedError("API_KEY is not set")

@app.get("/")
def read_index():
    return {"hello": "world goyi spot cuis cuis", "project_name": MY_PROJECT}