from repositorios.interfaces.usuario import IRepositorioUsuario
from esquemas.usuario import CrearUsuario, RespuestaUsuario
from servicios.interfaces.usuario import IServicioUsuario

class ServicioUsuario(IServicioUsuario):
    def __init__(self, repositorio: IRepositorioUsuario):
        self.repositorio = repositorio

    def crear_usuario(self, usuario: CrearUsuario) -> RespuestaUsuario:
        return self.repositorio.insertar_usuario(usuario)

    def obtener_todos_los_usuarios(self) -> list[RespuestaUsuario]:
        return self.repositorio.obtener_todos_los_usuarios()
