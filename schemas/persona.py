from datetime import datetime
from typing import Optional
from pydantic import BaseModel

class Persona(BaseModel):
    id:Optional[str]
    apellido:str
    nombre:str
    dni:str
    fechaNac:str
    direccion:str
    provincia_id:int
    