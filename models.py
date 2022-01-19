from uuid import UUID
from typing import Optional, List
from uuid import UUID, uuid4
from pydantic import BaseModel
from enum import Enum


class Status(str, Enum):
    ligado = "ligado"
    desligado = "desligado"


class Eletronic(BaseModel):
    id: Optional[UUID] = uuid4()
    name: Optional[str]
    comodo: Optional[str]
    ip_adress: Optional[str]
    status: Status
    consumo_medio: Optional[str]
    consumo_atual: Optional[str]

class EletronicUpdateRequest(BaseModel):
    name: Optional[str]
    comodo: Optional[str]
    ip_adress: Optional[str]
    status: Status
    consumo_medio: Optional[str]
    consumo_atual: Optional[str]

