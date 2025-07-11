import os

from fastapi import APIRouter, Depends, HTTPException, Query
from servicios.interfaces.obtener import IServicioObtener
from dependencias import obtener_servicio_obtener
from typing import Optional

router = APIRouter(
    prefix="/obtener",
    tags=["Obtener"]
)

@router.get("/proyectos", operation_id="get_projects")
def obtener_proyectos(servicio: IServicioObtener = Depends(obtener_servicio_obtener)):
    return servicio.obtener_proyectos()

@router.get("/carpeta", operation_id="get_folder_content")
def obtener_contenido_carpeta(
    ruta_carpeta: str = Query(os.getenv("CARPETA_RAIZ_PROYECTOS", "/Users/jevdev2304/Documents/CIC"), description="Ruta absoluta de la carpeta a listar"),
    servicio: IServicioObtener = Depends(obtener_servicio_obtener)
):
    return servicio.obtener_contenido_carpeta(ruta_carpeta)

@router.get("/buscar/archivo", operation_id="search_file_by_name_or_extension")
def buscar_archivo(
    nombre: Optional[str] = Query(None, description="Nombre o parte del nombre del archivo"),
    extension: Optional[str] = Query(None, description="Extensión del archivo, por ejemplo .py"),
    servicio: IServicioObtener = Depends(obtener_servicio_obtener)
):
    return servicio.buscar_archivo(nombre, extension)

@router.get("/metadatos/archivo", operation_id="get_file_metadata_by_path")
def metadatos_archivo(
    ruta: str = Query(..., description="Ruta absoluta del archivo"),
    servicio: IServicioObtener = Depends(obtener_servicio_obtener)
):
    return servicio.metadatos_archivo(ruta)

@router.get("/archivos/{archivo:path}", operation_id="read_file")
def leer_archivo(archivo: str, servicio: IServicioObtener = Depends(obtener_servicio_obtener)):
    return servicio.leer_archivo(archivo)




