from abc import ABC, abstractmethod
from esquemas.producto import CrearProducto, RespuestaProducto
from typing import List

class IRepositorioProducto(ABC):
    @abstractmethod
    def insertar_producto(self, producto: CrearProducto) -> RespuestaProducto:
        pass

    @abstractmethod
    def obtener_producto(self, id_producto: int) -> RespuestaProducto:
        pass

    @abstractmethod
    def obtener_productos_de_usuario(self,id_usuario:int) -> List[RespuestaProducto]:
        pass
