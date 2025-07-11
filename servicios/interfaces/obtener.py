from abc import ABC, abstractmethod
from typing import List, Optional

class IServicioObtener(ABC):
    @abstractmethod
    def obtener_proyectos(self, ruta: str = "/var/www") -> List[dict]:
        pass
    
    @abstractmethod
    def obtener_contenido_carpeta(self, ruta_carpeta: str) -> List[dict]:
        pass
    
    @abstractmethod
    def leer_archivo(self, archivo: str) -> dict:
        pass

    @abstractmethod
    def buscar_archivo(self, nombre: Optional[str] = None, extension: Optional[str] = None) -> List[dict]:
        pass

    @abstractmethod
    def metadatos_archivo(self, ruta: str) -> dict:
        pass

    @abstractmethod
    def obtener_estructura_completa_texto(self, ruta_base: str) -> str:
        pass