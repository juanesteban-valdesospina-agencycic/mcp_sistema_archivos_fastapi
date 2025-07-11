from fastapi import APIRouter, UploadFile, File, Form, HTTPException, Depends, Body
from pydantic import BaseModel
from dependencias import obtener_servicio_crear
from servicios.interfaces.crear import IServicioCrear
from pathlib import Path

router = APIRouter(
    prefix="/crear",
    tags=["Crear"]
)

@router.post("/archivo/upload", operation_id="create_or_overwrite_file_using_upload")
def crear_o_sobrescribir_archivo_upload(
    carpeta_destino: str = Form(...),
    archivo: UploadFile = File(...),
    servicio: IServicioCrear = Depends(obtener_servicio_crear)
):
    return servicio.crear_o_sobrescribir_archivo(carpeta_destino, archivo)

class ArchivoTextoDTO(BaseModel):
    carpeta_destino: str
    nombre_archivo: str
    contenido: str

@router.post("/archivo/texto", operation_id="create_or_overwrite_file_using_text")
def crear_o_sobrescribir_archivo_texto(
    datos: ArchivoTextoDTO = Body(...),
    servicio: IServicioCrear = Depends(obtener_servicio_crear)
):
    return servicio.crear_o_sobrescribir_archivo_texto(
        datos.carpeta_destino, datos.nombre_archivo, datos.contenido
    )

class RenombrarArchivoDTO(BaseModel):
    ruta_actual: str
    nuevo_nombre: str

@router.post("/archivo/renombrar", operation_id="rename_file_by_path")
def renombrar_archivo(
    datos: RenombrarArchivoDTO = Body(...),
    servicio: IServicioCrear = Depends(obtener_servicio_crear)
):
    return servicio.renombrar_archivo(datos.ruta_actual, datos.nuevo_nombre)
