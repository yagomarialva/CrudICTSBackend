from fastapi import FastAPI
from models import Eletronic, EletronicUpdateRequest, Status
from typing import List
from typing import List
from uuid import UUID, uuid4
from fastapi import FastAPI, HTTPException

app = FastAPI()

db: List[Eletronic] = [
    Eletronic(
        id=uuid4(),
        name="Smart TV",
        comodo="Sala",
        ip_adress="192.157.0.1",
        status=Status.ligado,
        consumo_medio="145k",
        consumo_atual="20kw"
    )
]


@app.get("/")
async def root():
    return {"Hello": "World"}


@app.get("/api/v1/eletronics")
async def fetch_eletronics():
    return db



@app.post("/api/v1/eletronics")
async def fetch_eletronics(eletronic: Eletronic):
    db.append(eletronic)
    return {"id": eletronic.id}

@app.delete("/api/v1/eletronics/{eletronics_id_id}")
async def delete_eletronics(eletronics_id: UUID):
    for eletronics in db:
        if eletronics.id == eletronics_id:
            db.remove(eletronics)
            return
    raise HTTPException(
        status_code=404,
        detail=f"eletronics with id: {eletronics_id} does not exists")


@app.put("/api/v1/eletronics/{eletronics_id_id}")
async def update_eletronics_id(eletronics_id_update: EletronicUpdateRequest, eletronics_id_id: UUID):
    for eletronics_id in db:
        if eletronics_id.id == eletronics_id_id:
            if eletronics_id_update.name is not None:
                eletronics_id.name = eletronics_id_update.name
            if eletronics_id_update.comodo is not None:
                eletronics_id.comodo = eletronics_id_update.comodo
            if eletronics_id_update.ip_adress is not None:
                eletronics_id.ip_adress = eletronics_id_update.ip_adress
            if eletronics_id_update.status is not None:
                eletronics_id.status = eletronics_id_update.status
            if eletronics_id_update.consumo_medio is not None:
                eletronics_id.consumo_medio = eletronics_id_update.consumo_medio
            if eletronics_id_update.consumo_atual is not None:
                eletronics_id.consumo_atual = eletronics_id_update.consumo_atual
            return
        raise HTTPException(
            status_code=404,
            detail=f"eletronics_id with id: {eletronics_id_id} does not exists")