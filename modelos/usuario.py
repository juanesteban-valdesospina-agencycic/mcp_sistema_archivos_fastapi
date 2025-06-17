from datetime import datetime

from pydantic import BaseModel, EmailStr

class Usuario(BaseModel):
    id: int
    nombre_usuario: str
    correo_electronico: EmailStr
    contrasena: str
    fecha_creacion: datetime