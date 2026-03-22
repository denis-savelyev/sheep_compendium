from fastapi import FastAPI, status, HTTPException
from models.db import db
from models.models import Sheep

app = FastAPI()

@app.get("/sheep/{id}", response_model=Sheep)
def read_sheep(id: int):
    return db.get_sheep(id)

@app.post("/sheep/", response_model=Sheep, status_code=status.HTTP_201_CREATED)
def add_sheep(sheep: Sheep):

    if sheep.id in db.data:
        raise HTTPException(status_code=400, detail=f"Sheep with id {sheep.id} already exists.")

    db.add_sheep(sheep.id, sheep)
    return sheep

@app.delete("/sheep/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_sheep(id: int):
    if id not in db.data:
        raise HTTPException(status_code=404, detail=f"Sheep with id {id} does not exist.")

    db.del_sheep(id)