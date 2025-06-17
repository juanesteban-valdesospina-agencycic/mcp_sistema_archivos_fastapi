from typing import List

from repositorios.interfaces.producto import IRepositorioProducto
from esquemas.producto import CrearProducto, RespuestaProducto


class ServicioProducto:
    def __init__(self, repositorio: IRepositorioProducto):
        self.repositorio = repositorio

    def crear_producto(self, producto: CrearProducto) -> RespuestaProducto:
        return self.repositorio.insertar_producto(producto)

    def obtener_producto(self, id_producto: int) -> RespuestaProducto:
        return self.repositorio.obtener_producto(id_producto)

    def obtener_productos_usuario(self, id_usuario:int) -> List[RespuestaProducto]:
        return self.repositorio.obtener_productos_de_usuario(id_usuario)
