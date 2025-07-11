# main.py
from fastapi import FastAPI, Depends
from enrutadores.obtener import router as obtener_router
from enrutadores.crear import router as crear_router
from enrutadores.eliminar import router as eliminar_router
from fastapi_mcp import FastApiMCP
import uvicorn
app = FastAPI()
app.include_router(obtener_router)
app.include_router(crear_router)
app.include_router(eliminar_router)
mcp = FastApiMCP(app, include_operations=["get_projects", "get_project_files", "read_file",  "delete_file_or_folder", "get_folder_content", "create_or_overwrite_file_using_text","rename_file_by_path","search_file_by_name_or_extension", "get_file_metadata_by_path"])
mcp.mount()


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)