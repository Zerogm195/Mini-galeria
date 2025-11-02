from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import json

#Por cada imagen

app = FastAPI()

@app.get("/")
def leerJson():
    with open("data.json", "r") as f:
        datos = json.load(f)

        return datos

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # o solo tu frontend
    allow_methods=["*"],
    allow_headers=["*"],
)