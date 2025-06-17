from abc import ABC, abstractmethod
from typing import List
from esquemas.producto import CrearProducto, RespuestaProducto

class IServicioProducto(ABC):
    @abstractmethod
    def crear_producto(self, producto: CrearProducto) -> RespuestaProducto:
        pass

    @abstractmethod
    def obtener_producto(self, id_producto: int) -> RespuestaProducto:
        pass

    @abstractmethod
    def obtener_productos_usuario(self, id_usuario: int) -> List[RespuestaProducto]:
        pass
