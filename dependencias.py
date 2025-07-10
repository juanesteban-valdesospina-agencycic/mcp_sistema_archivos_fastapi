from servicios.interfaces.obtener import IServicioObtener
from servicios.obtener import ServicioObtener
from servicios.crear import ServicioCrear
from servicios.eliminar import ServicioEliminar

def obtener_servicio_obtener() -> IServicioObtener:
    return ServicioObtener()

def obtener_servicio_crear():
    return ServicioCrear()

def obtener_servicio_eliminar():
    return ServicioEliminar()