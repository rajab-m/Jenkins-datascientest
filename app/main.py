from typing import Union
from fastapi import FastAPI
app = FastAPI()
@app.get("/")
def read_root():
    return {"Hellooo": "We Love Datascientest, and we did it. We build a CI/CD Pipeline!!"}

