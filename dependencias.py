from db import get_connection
from servicios.usuario import ServicioUsuario
from repositorios.usuario import RepositorioUsuario
from servicios.interfaces.usuario import IServicioUsuario
from servicios.interfaces.producto import IServicioProducto
from servicios.producto import ServicioProducto
from repositorios.producto import RepositorioProducto

def obtener_servicio_usuario() -> IServicioUsuario:
    conn, cursor = get_connection()
    return ServicioUsuario(RepositorioUsuario(conn, cursor))

def obtener_servicio_producto() -> IServicioProducto:
    conn, cursor = get_connection()
    return ServicioProducto(RepositorioProducto(conn, cursor))