from abc import ABC, abstractmethod

class IServicioEliminar(ABC):
    @abstractmethod
    def eliminar(self, ruta_objetivo: str) -> dict:
        pass
