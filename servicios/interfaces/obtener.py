from abc import ABC, abstractmethod

class Obtener(ABC):
    @abstractmethod
    def obtener_proyectos(self):
        pass