# main.py
from fastapi import FastAPI, Depends
from db import get_connection
from mysql.connector import MySQLConnection
from enrutadores.usuarios import router as usuario_router
from enrutadores.productos import router as producto_router
import uvicorn
app = FastAPI()
app.include_router(usuario_router)
app.include_router(producto_router)



if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)