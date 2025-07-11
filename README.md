# 📁 MCP FastAPI

**MCP FastAPI** es una API construida con [FastAPI](https://fastapi.tiangolo.com/) para gestionar archivos dentro de una carpeta específica del sistema. Permite explorar, leer, escribir, modificar, eliminar y renombrar archivos, ideal para proyectos que requieren acceso controlado al filesystem.

---

## 🚀 Funcionalidades principales

| Funcionalidad | Descripción |
|---------------|-------------|
| `get_projects` | Lista las carpetas de nivel superior (proyectos). |
| `get_project_files` | Lista los archivos dentro de un proyecto. |
| `read_file` | Lee el contenido de un archivo dado su path. |
| `delete_file_or_folder` | Elimina un archivo o carpeta. |
| `get_folder_content` | Muestra el contenido de una carpeta específica. |
| `create_or_overwrite_file_using_text` | Crea o sobrescribe un archivo con texto. |
| `rename_file_by_path` | Renombra un archivo o carpeta. |
| `search_file_by_name_or_extension` | Busca archivos por nombre o extensión. |
| `get_file_metadata_by_path` | Devuelve información como tamaño, tipo y fechas. |

Todos los endpoints pueden ser consumidos mediante HTTP con peticiones estándar (`GET`, `POST`, `DELETE`, etc.), lo que permite integrarlos fácilmente con interfaces web, scripts o herramientas externas.

---

# 🔧 FastMCP

**FastMCP** es un módulo auxiliar que convierte una aplicación FastAPI en una API MCP con rutas predefinidas para la gestión de archivos.

Permite:

- Registrar automáticamente todos los endpoints MCP.
- Configurar de forma rápida la ruta base del filesystem.
- Usarlo como extensión en cualquier proyecto FastAPI.

---

## ▶️ Ejecución rápida

```bash
uvicorn main:app --reload
