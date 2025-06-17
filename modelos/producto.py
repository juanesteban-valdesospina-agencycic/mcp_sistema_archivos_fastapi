from datetime import datetime

from pydantic import BaseModel

class Producto(BaseModel):
    id: int
    nombre: str
    descripcion:str
    precio: float
    stock: int
    usuario_id: int
    fecha_creacion: datetime