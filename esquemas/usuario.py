from datetime import datetime

from pydantic import BaseModel, EmailStr

class CrearUsuario(BaseModel):
    nombre_usuario: str
    correo_electronico: EmailStr
    contrasena: str

class RespuestaUsuario(BaseModel):
    id: int
    nombre_usuario: str
    correo_electronico: EmailStr
    fecha_creacion: datetime
