from fastapi import APIRouter, Depends, Body
from pydantic import BaseModel
from dependencias import obtener_servicio_eliminar
from servicios.interfaces.eliminar import IServicioEliminar

router = APIRouter(
    prefix="/eliminar",
    tags=["Eliminar"]
)

class EliminarDTO(BaseModel):
    ruta_objetivo: str

@router.post("/objeto", operation_id="delete_file_or_folder")
def eliminar_objeto(
    datos: EliminarDTO = Body(...),
    servicio: IServicioEliminar = Depends(obtener_servicio_eliminar)
):
    return servicio.eliminar(datos.ruta_objetivo)
