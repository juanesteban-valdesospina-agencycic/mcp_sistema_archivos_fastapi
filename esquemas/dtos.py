#1 LIBRERIAS INTERNAS DE PYTHON
from datetime import date
#2 LIBRERIAS EXTERNAS DE PYTHON
from pydantic import BaseModel
from typing import Optional
#3 IMPORTACIONES DE MODULOS PROPIOS
from modelos.producto import Producto

class CrearProducto(BaseModel):
    nombre: str
    descripcion:str
    precio: float
    stock: int
    usuario_id: int
    fecha_creacion: Optional[date] = date.today()

class RespuestaProducto(Producto):
    pass
