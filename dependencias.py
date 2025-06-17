from db import get_connection
from servicios.usuario import ServicioUsuario
from repositorios.usuario import RepositorioUsuario
from servicios.producto import ServicioProducto
from repositorios.producto import RepositorioProducto

def obtener_servicio_usuario() -> ServicioUsuario:
    conn, cursor = get_connection()
    return ServicioUsuario(RepositorioUsuario(conn, cursor))

def obtener_servicio_producto() -> ServicioProducto:
    conn, cursor = get_connection()
    return ServicioProducto(RepositorioProducto(conn, cursor))