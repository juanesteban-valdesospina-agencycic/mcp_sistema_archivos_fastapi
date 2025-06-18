from typing import List

from repositorios.interfaces.producto import IRepositorioProducto
from esquemas.producto import CrearProducto, RespuestaProducto
class RepositorioProducto(IRepositorioProducto):
    def __init__(self, conn, cursor):
        self.conn = conn
        self.cursor = cursor

    def insertar_producto(self, producto: CrearProducto) -> RespuestaProducto:
        try:
            sql = """
                INSERT INTO productos (nombre, descripcion, precio, stock, usuario_id)
                VALUES (%s, %s, %s, %s, %s)
            """
            valores = (producto.nombre, producto.descripcion, producto.precio, producto.stock, producto.usuario_id)
            self.cursor.execute(sql, valores)
            self.conn.commit()
            nuevo_id = self.cursor.lastrowid
            self.cursor.execute("SELECT * FROM productos WHERE id = %s", (nuevo_id,))
            fila = self.cursor.fetchone()
            return RespuestaProducto(**fila)
        except Exception as e:
            self.conn.rollback()
            raise e
        finally:
            self.cursor.close()
            self.conn.close()

    def obtener_producto(self, id_producto: int) -> RespuestaProducto:
        try:
            sql = "SELECT * FROM productos WHERE id = %s"
            self.cursor.execute(sql, (id_producto,))
            fila = self.cursor.fetchone()

            if not fila:
                raise ValueError(f"No se encontró un producto con id {id_producto}")

            return RespuestaProducto(**fila)
        except Exception as e:
            self.conn.rollback()
            raise e
        finally:
            self.cursor.close()
            self.conn.close()

    def obtener_productos_de_usuario(self, id_usuario: int) -> List[RespuestaProducto]:
        try:
            sql = "SELECT * FROM productos WHERE usuario_id = %s"
            self.cursor.execute(sql, (id_usuario,))
            filas = self.cursor.fetchall()

            return [RespuestaProducto(**fila) for fila in filas]
        except Exception as e:
            self.conn.rollback()
            raise e
        finally:
            self.cursor.close()
            self.conn.close()

