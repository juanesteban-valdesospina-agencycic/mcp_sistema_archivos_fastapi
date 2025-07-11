
# 🚀 **FastAPI MCP Server - Sistema de Gestión de Archivos**

Un servidor FastAPI que utiliza FastMCP para convertir endpoints de gestión de archivos en un servidor MCP (Model Context Protocol), permitiendo integración directa con herramientas de IA como GitHub Copilot, Claude y Cursor.

## 📋 **Características**

- ✅ **Gestión de archivos** - Operaciones CRUD completas
- ✅ **Navegación de directorios** - Exploración del sistema de archivos
- ✅ **Búsqueda de archivos** - Por nombre, extensión y patrón
- ✅ **Metadatos** - Información detallada de archivos
- ✅ **FastMCP Integration** - Conversión automática de endpoints a MCP
- ✅ **Validación de rutas** - Seguridad en operaciones de archivos

## 🏗️ **Tecnologías**

- **FastAPI** - Framework web principal
- **FastMCP** - Conversión de endpoints a protocolo MCP
- **Python 3.8+** - Lenguaje base

## 🚀 **Instalación**

```bash
# Instalar dependencias
pip install fastapi uvicorn fastmcp

# Ejecutar servidor
uvicorn main:app --host 0.0.0.0 --port 8000
```

## 🔌 **Configuración MCP**

Agregar al archivo `settings.json`:
```json
{
    "mcp": {
        "servers": {
            "fastapi_mcp": {
                "url": "http://0.0.0.0:8000/mcp"
            }
        }
    }
}
```

## 📚 **Funcionalidades MCP Disponibles**

### **Exploración**
- `get_projects` - Lista proyectos detectados
- `get_folder_content` - Contenido de directorios

### **Gestión de Archivos**
- `read_file` - Leer contenido de archivos
- `create_or_overwrite_file_using_text` - Crear/sobrescribir archivos
- `delete_file_or_folder` - Eliminar archivos o carpetas

### **Búsqueda y Metadatos**
- `search_files` - Buscar archivos por patrón
- `get_file_metadata` - Información detallada
- `rename_file` - Renombrar archivos

## 🌐 **Endpoints REST**

| **Método** | **Endpoint** | **Función MCP** |
|------------|--------------|-----------------|
| `GET` | `/proyectos` | `get_projects` |
| `GET` | `/contenido/` | `get_folder_content` |
| `GET` | `/archivo/` | `read_file` |
| `POST` | `/crear/archivo` | `create_or_overwrite_file_using_text` |
| `DELETE` | `/eliminar/objeto` | `delete_file_or_folder` |
| `GET` | `/buscar` | `search_files` |
| `GET` | `/metadatos/` | `get_file_metadata` |
| `PUT` | `/renombrar` | `rename_file` |

## 📖 **Ejemplo de Uso**

### **Via MCP (GitHub Copilot, Claude, etc.)**
```python
# Las herramientas de IA pueden llamar directamente:
projects = get_projects()
content = read_file("/path/to/file.txt")
search_results = search_files("*.py", "/project")
```

### **Via REST API**
```bash
# Listar proyectos
curl http://localhost:8000/proyectos

# Leer archivo
curl http://localhost:8000/archivo/?file_path=/path/to/file.txt

# Buscar archivos
curl "http://localhost:8000/buscar?search_pattern=*.txt"
```

## 🔧 **FastMCP - Conversión Automática**

FastMCP convierte automáticamente cada endpoint REST en una herramienta MCP:

```python
# Endpoint FastAPI
@app.get("/archivo/")
def read_file_endpoint(file_path: str):
    return read_file_logic(file_path)

# Se convierte automáticamente en herramienta MCP
@mcp_server.tool
def read_file(file_path: str):
    # Misma lógica, protocolo MCP
```

## 🛡️ **Seguridad**

- Validación de rutas para prevenir acceso no autorizado
- Sanitización de parámetros de entrada
- Manejo de errores y excepciones

## 📊 **Estado Actual**

| **Funcionalidad** | **Estado** |
|-------------------|------------|
| Exploración de archivos | ✅ Funcional |
| Lectura de archivos | ✅ Funcional |
| Creación de archivos | ✅ Funcional |
| Eliminación de archivos | ✅ Funcional |
| Búsqueda de archivos | ✅ Funcional |
| Metadatos | ✅ Funcional |
| Renombrado | ✅ Funcional |

## 🎯 **Casos de Uso**

- **Desarrollo remoto** - Gestión de archivos sin SSH
- **Integración con IA** - Herramientas como Copilot pueden gestionar archivos
- **Automatización** - Scripts y herramientas pueden usar la API

---

**FastAPI MCP Server** - Convierte tu API de archivos en un servidor MCP con FastMCP. 🚀
