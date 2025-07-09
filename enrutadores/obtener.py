from fastapi import APIRouter, Depends, HTTPException

from esquemas.producto import CrearProducto, RespuestaProducto
from servicios.producto import ServicioProducto
from dependencias import obtener_servicio_producto

router = APIRouter(
    prefix="/productos",
    tags=["Productos"]
)

@router.post(
    "/",
    response_model=RespuestaProducto,
    summary="Crear un nuevo producto",
    description="Permite crear un producto nuevo enviando los datos requeridos en el cuerpo de la solicitud.",
    response_description="Producto creado con todos sus datos, incluyendo el ID generado."
)
def crear_producto(producto: CrearProducto, servicio: ServicioProducto = Depends(obtener_servicio_producto)):
    try:
        return servicio.crear_producto(producto)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.get(
    "/{id_producto}",
    response_model=RespuestaProducto,
    summary="Obtener producto por ID",
    description="Devuelve los detalles completos de un producto específico dado su ID.",
    responses={
        404: {"description": "Producto no encontrado."}
    }
)
def obtener_producto(id_producto: int, servicio: ServicioProducto = Depends(obtener_servicio_producto)):
    try:
        return servicio.obtener_producto(id_producto)
    except Exception as e:
        raise HTTPException(status_code=404, detail=str(e))


@router.get(
    "/usuario/{id_usuario}",
    response_model=list[RespuestaProducto],
    summary="Obtener productos de un usuario",
    description="Obtiene una lista con todos los productos creados por un usuario específico, identificado por su ID.",
    responses={
        404: {"description": "No se encontraron productos para este usuario."}
    }
)
def obtener_productos_usuario(id_usuario: int, servicio: ServicioProducto = Depends(obtener_servicio_producto)):
    try:
        return servicio.obtener_productos_usuario(id_usuario)
    except Exception as e:
        raise HTTPException(status_code=404, detail=str(e))
