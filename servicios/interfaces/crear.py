from abc import ABC, abstractmethod
from fastapi import UploadFile

class IServicioCrear(ABC):
    @abstractmethod
    def crear_o_sobrescribir_archivo(self, carpeta_destino: str, archivo: UploadFile) -> dict:
        pass

    @abstractmethod
    def crear_o_sobrescribir_archivo_texto(self, carpeta_destino: str, nombre_archivo: str, contenido: str) -> dict:
        pass
