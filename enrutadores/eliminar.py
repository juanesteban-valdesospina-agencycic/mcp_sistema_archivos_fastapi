from fastapi import APIRouter, Form, Depends
from dependencias import obtener_servicio_eliminar
from servicios.interfaces.eliminar import IServicioEliminar

router = APIRouter(
    prefix="/eliminar",
    tags=["Eliminar"]
)

@router.delete("/archivo", operation_id="delete_file")
def eliminar_objeto(
    ruta_objetivo: str = Form(...),
    servicio: IServicioEliminar = Depends(obtener_servicio_eliminar)
):
    return servicio.eliminar(ruta_objetivo)
