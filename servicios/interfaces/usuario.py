from abc import ABC, abstractmethod
from esquemas.usuario import CrearUsuario, RespuestaUsuario
from typing import List

class IServicioUsuario(ABC):
    @abstractmethod
    def crear_usuario(self, usuario: CrearUsuario) -> RespuestaUsuario:
        pass

    @abstractmethod
    def obtener_todos_los_usuarios(self) -> List[RespuestaUsuario]:
        pass
