from typing import Optional
from pydantic import BaseModel

class Provincia(BaseModel):
    id:Optional[str]
    name:str