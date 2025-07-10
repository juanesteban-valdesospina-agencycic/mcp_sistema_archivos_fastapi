from servicios.interfaces.eliminar import IServicioEliminar
from fastapi import HTTPException
from pathlib import Path
import shutil

class ServicioEliminar(IServicioEliminar):
    def eliminar(self, ruta_objetivo: str) -> dict:
        ruta_base = Path("/Users/jevdev2304/Documents/CIC").resolve()
        objetivo = Path(ruta_objetivo).resolve()
        # Validar que la ruta objetivo esté dentro de la carpeta de proyectos
        try:
            objetivo.relative_to(ruta_base)
        except ValueError:
            raise HTTPException(status_code=403, detail="No tienes permiso para eliminar fuera de la carpeta de proyectos.")
        if not objetivo.exists():
            raise HTTPException(status_code=404, detail="El archivo o carpeta no existe.")
        try:
            if objetivo.is_file():
                objetivo.unlink()
                return {"mensaje": f"Archivo '{objetivo}' eliminado exitosamente."}
            elif objetivo.is_dir():
                shutil.rmtree(objetivo)
                return {"mensaje": f"Carpeta '{objetivo}' eliminada exitosamente."}
            else:
                raise HTTPException(status_code=400, detail="La ruta objetivo no es un archivo ni una carpeta.")
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Error al eliminar: {e}")
