import os
from dotenv import load_dotenv
load_dotenv()

from pathlib import Path
from typing import List, Optional
from servicios.interfaces.obtener import IServicioObtener


class ServicioObtener(IServicioObtener):
    def obtener_proyectos(self, ruta: str = "/Users/jevdev2304/Documents/CIC") -> List[dict]:
        p = Path(ruta)
        if not p.exists() or not p.is_dir():
            return []
        return [
            {"nombre": f.name, "ruta": str(f.resolve())}
            for f in p.iterdir() if f.is_dir()
        ]

    def obtener_contenido_carpeta(self, ruta_carpeta: str) -> List[dict]:
        ruta_base = Path("/Users/jevdev2304/Documents/CIC").resolve()
        carpeta = Path(ruta_carpeta).resolve()
        try:
            carpeta.relative_to(ruta_base)
        except ValueError:
            return []
        if not carpeta.exists() or not carpeta.is_dir():
            return []
        resultado = []
        for f in carpeta.iterdir():
            if f.is_file():
                resultado.append({
                    "nombre": f.name,
                    "ruta": str(f.resolve()),
                    "tipo": "archivo"
                })
            elif f.is_dir():
                resultado.append({
                    "nombre": f.name,
                    "ruta": str(f.resolve()),
                    "tipo": "carpeta"
                })
        return resultado

    def leer_archivo(self, archivo: str) -> dict:
        p = Path(archivo)
        if not p.exists() or not p.is_file():
            return {"nombre": p.name, "ruta": str(p.resolve()), "contenido": None}
        return {"nombre": p.name, "ruta": str(p.resolve()), "contenido": p.read_text()}

    def buscar_archivo(self, nombre: Optional[str] = None, extension: Optional[str] = None) -> List[dict]:
        ruta_base = Path(os.getenv("CARPETA_RAIZ_PROYECTOS", "/Users/jevdev2304/Documents/CIC")).resolve()
        resultados = []
        for root, dirs, files in os.walk(ruta_base):
            for file in files:
                if nombre and nombre not in file:
                    continue
                if extension and not file.endswith(extension):
                    continue
                resultados.append({
                    "nombre": file,
                    "ruta": str(Path(root) / file)
                })
        return resultados

    def metadatos_archivo(self, ruta: str) -> dict:
        p = Path(ruta)
        if not p.exists():
            return {"error": "El archivo no existe"}
        stat = p.stat()
        return {
            "nombre": p.name,
            "ruta": str(p.resolve()),
            "tamano": stat.st_size,
            "ultima_modificacion": stat.st_mtime,
            "tipo": "carpeta" if p.is_dir() else "archivo"
        }


    def obtener_estructura_completa_texto(self, ruta_base: Optional[str] = None) -> str:
        import json
        """
        Genera un árbol del directorio dado, ignorando carpetas típicas de entornos Python y Node.
        Retorna un JSON anidado como string.
        """
        if ruta_base is None:
            ruta_base = os.getenv("CARPETA_RAIZ_PROYECTOS", "/Users/jevdev2304/Documents/CIC")
        IGNORAR = {"node_modules", ".venv", "venv", "__pycache__", ".git", ".mypy_cache", ".pytest_cache", ".idea", ".vscode"}
        try:
            base = Path(ruta_base).resolve(strict=True)
            if not base.is_dir():
                return json.dumps({"error": "La ruta proporcionada no es un directorio."})
        except FileNotFoundError:
            return json.dumps({"error": "Directorio raíz no existe."})
        except Exception as e:
            return json.dumps({"error": f"Error inesperado al acceder a la ruta base: {e}"})

        def seguro_en_base(path: Path) -> bool:
            try:
                return path.resolve().is_relative_to(base)
            except Exception:
                return False

        def recorrer_arbol_json(directorio: Path):
            contenido = []
            try:
                items = sorted(directorio.iterdir())
            except Exception:
                return [{"nombre": "[Acceso denegado o error]", "tipo": "error"}]
            for path in items:
                if path.name in IGNORAR:
                    continue
                if not seguro_en_base(path):
                    continue
                if path.is_dir():
                    contenido.append({
                        "nombre": path.name,
                        "tipo": "carpeta",
                        "contenido": recorrer_arbol_json(path)
                    })
                else:
                    contenido.append({
                        "nombre": path.name,
                        "tipo": "archivo"
                    })
            return contenido

        estructura = {
            "nombre": base.name,
            "tipo": "carpeta",
            "contenido": recorrer_arbol_json(base)
        }
        return json.dumps(estructura, ensure_ascii=False)
