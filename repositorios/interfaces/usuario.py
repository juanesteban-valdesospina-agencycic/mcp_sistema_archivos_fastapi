from abc import ABC, abstractmethod

from typing import List

from esquemas.usuario import CrearUsuario, RespuestaUsuario

class IRepositorioUsuario(ABC):
    @abstractmethod
    def insertar_usuario(self, usuario: CrearUsuario) -> RespuestaUsuario:
        pass

    @abstractmethod
    def obtener_todos_los_usuarios(self) -> List[RespuestaUsuario]:
        pass
