import os
from dotenv import load_dotenv
load_dotenv()

from fastapi import UploadFile, HTTPException
from pathlib import Path
from servicios.interfaces.crear import IServicioCrear

class ServicioCrear(IServicioCrear):
    def crear_o_sobrescribir_archivo(self, carpeta_destino: str, archivo: UploadFile) -> dict:
        ruta_base = Path(os.getenv("CARPETA_RAIZ_PROYECTOS", "/Users/jevdev2304/Documents/CIC"))
        proyecto = str(carpeta_destino or "")
        if not archivo.filename:
            raise HTTPException(status_code=400, detail="El archivo debe tener un nombre válido.")
        carpeta = Path(carpeta_destino).resolve()
        try:
            carpeta.relative_to(ruta_base)
        except Exception:
            raise HTTPException(status_code=403, detail="No tienes permiso para escribir fuera de la carpeta de proyectos.")
        if not carpeta.exists() or not carpeta.is_dir():
            raise HTTPException(status_code=404, detail=f"La carpeta destino '{carpeta_destino}' no existe o no es un directorio.")
        destino = carpeta / archivo.filename
        try:
            with open(destino, "wb") as f:
                contenido = archivo.file.read()
                f.write(contenido)
            return {"mensaje": "Archivo creado/sobrescrito exitosamente", "ruta": str(destino)}
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Error al guardar el archivo: {e}")

    def crear_o_sobrescribir_archivo_texto(self, carpeta_destino: str, nombre_archivo: str, contenido: str) -> dict:
        ruta_base = Path(os.getenv("CARPETA_RAIZ_PROYECTOS", "/Users/jevdev2304/Documents/CIC")).resolve()
        carpeta = Path(carpeta_destino).resolve()
        try:
            carpeta.relative_to(ruta_base)
        except Exception:
            raise HTTPException(status_code=403, detail="No tienes permiso para escribir fuera de la carpeta de proyectos.")
        if not carpeta.exists() or not carpeta.is_dir():
            raise HTTPException(status_code=404, detail=f"La carpeta destino '{carpeta_destino}' no existe o no es un directorio.")
        destino = carpeta / nombre_archivo
        try:
            with open(destino, "w", encoding="utf-8") as f:
                f.write(contenido)
            return {"mensaje": "Archivo creado/sobrescrito exitosamente", "ruta": str(destino)}
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Error al guardar el archivo: {e}")
