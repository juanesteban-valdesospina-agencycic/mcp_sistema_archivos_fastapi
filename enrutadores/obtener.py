from fastapi import APIRouter, Depends, HTTPException

router = APIRouter(
    prefix="/obtener",
    tags=["Obtener"]
)

@router.get("/")
def obtener_ruta_proyectos():
    pass


