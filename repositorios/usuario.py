from repositorios.interfaces.usuario import IRepositorioUsuario
from esquemas.usuario import CrearUsuario, RespuestaUsuario


class RepositorioUsuario(IRepositorioUsuario):
    def __init__(self, conn, cursor):
        self.conn = conn
        self.cursor = cursor

    def insertar_usuario(self, usuario: CrearUsuario) -> RespuestaUsuario:
        try:
            sql = """
                INSERT INTO usuarios (nombre_usuario, correo_electronico, contrasena)
                VALUES (%s, %s, %s)
            """
            valores = (usuario.nombre_usuario, usuario.correo_electronico, usuario.contrasena)
            self.cursor.execute(sql, valores)
            self.conn.commit()
            nuevo_id = self.cursor.lastrowid

            return RespuestaUsuario(
                id=nuevo_id,
                nombre_usuario=usuario.nombre_usuario,
                correo_electronico=usuario.correo_electronico
            )
        finally:
            self.cursor.close()
            self.conn.close()

    def obtener_todos_los_usuarios(self) -> list[RespuestaUsuario]:
        try:
            sql = "SELECT id, nombre_usuario, correo_electronico, fecha_creacion FROM usuarios"
            self.cursor.execute(sql)
            usuarios = self.cursor.fetchall()
            return [
                RespuestaUsuario(
                    id=usuario['id'],
                    nombre_usuario=usuario['nombre_usuario'],
                    correo_electronico=usuario['correo_electronico'],
                    fecha_creacion=usuario['fecha_creacion']
                ) for usuario in usuarios
            ]
        finally:
            self.cursor.close()
            self.conn.close()
