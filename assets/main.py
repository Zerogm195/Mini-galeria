from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import json
import listararchivos


app = FastAPI()

@app.get("/")
async def leerJson():
    listararchivos.obtenerDatos()

    with open(listararchivos.ruta_json, "r") as f:
        datos = json.load(f)

        return datos

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # o solo tu frontend
    allow_methods=["*"],
    allow_headers=["*"],
)