from fastapi import APIRouter, Depends, HTTPException
from esquemas.usuario import CrearUsuario, RespuestaUsuario
from servicios.usuario import ServicioUsuario
from dependencias import obtener_servicio_usuario

router = APIRouter(
    prefix="/usuarios",
    tags=["Usuarios"]
)

@router.post(
    "/",
    response_model=RespuestaUsuario,
    summary="Crear un nuevo usuario",
    description="Permite crear un usuario nuevo en el sistema proporcionando los datos requeridos."
)
def crear_usuario(usuario: CrearUsuario, servicio: ServicioUsuario = Depends(obtener_servicio_usuario)):
    try:
        return servicio.crear_usuario(usuario)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.get(
    "/",
    response_model=list[RespuestaUsuario],
    summary="Obtener todos los usuarios",
    description="Devuelve una lista con todos los usuarios registrados en el sistema."
)
def obtener_todos_los_usuarios(servicio: ServicioUsuario = Depends(obtener_servicio_usuario)):
    try:
        return servicio.obtener_todos_los_usuarios()
    except Exception as e:
        raise HTTPException(status_code=404, detail=str(e))
