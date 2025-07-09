# 📁 MCP Sistema de Archivos FastAPI

Un servidor Model Context Protocol (MCP) construido con FastAPI que proporciona operaciones seguras de sistema de archivos para integraciones con Claude Desktop y otros clientes MCP compatibles.

## 🎯 ¿Qué es este proyecto?

Este proyecto implementa un servidor MCP (Model Context Protocol) que permite a Claude Desktop y otros clientes compatibles realizar operaciones de sistema de archivos de manera segura y controlada. El servidor está construido con FastAPI y sigue una arquitectura limpia y modular.

### ¿Qué es MCP?

Model Context Protocol (MCP) es un protocolo estándar que permite a los modelos de IA acceder a recursos externos de manera segura. En este caso, proporciona acceso controlado al sistema de archivos local.

## ✨ Características

- 🔒 **Operaciones seguras**: Todas las operaciones están limitadas a directorios específicos autorizados
- 📂 **Gestión completa de archivos**: Crear, leer, actualizar, eliminar archivos y directorios
- 🔍 **Búsqueda de archivos**: Buscar archivos por nombre, extensión o contenido
- 📊 **Metadatos**: Obtener información detallada de archivos (tamaño, fecha, permisos)
- 🏗️ **Arquitectura modular**: Código organizado con separación clara de responsabilidades
- 🔌 **Compatible con MCP**: Integración nativa con Claude Desktop y otros clientes MCP
- 📋 **Validación robusta**: Esquemas Pydantic para validación de entrada y salida
- ⚡ **Alto rendimiento**: Construido con FastAPI para máxima velocidad

## 📁 Estructura del Proyecto

```
mcp_sistema_archivos_fastapi/
├── main.py                     # Punto de entrada de la aplicación MCP
├── enrutadores/
│   ├── crear.py               # Endpoints para crear archivos/directorios
│   ├── obtener.py             # Endpoints para leer y buscar archivos
│   ├── actualizar.py          # Endpoints para modificar archivos
│   └── eliminar.py            # Endpoints para eliminar archivos/directorios
├── servicios/
│   ├── interfaces/            # Interfaces de servicios
│   └── archivo_servicio.py    # Lógica de negocio para operaciones de archivos
├── esquemas/
│   ├── archivo.py             # Esquemas para operaciones de archivos
│   └── directorio.py          # Esquemas para operaciones de directorios
├── modelos/
│   ├── archivo.py             # Modelo de entidad archivo
│   └── directorio.py          # Modelo de entidad directorio
├── dependencias.py            # Inyección de dependencias
├── configuracion.py           # Configuración de seguridad y rutas permitidas
└── requirements.txt           # Dependencias del proyecto
```

## 🔧 Instalación y Configuración

### Prerrequisitos
- Python 3.8 o superior
- pip (gestor de paquetes de Python)

### Pasos de instalación

1. **Clonar el repositorio**
   ```bash
   git clone https://github.com/juanesteban-valdesospina-agencycic/mcp_sistema_archivos_fastapi.git
   cd mcp_sistema_archivos_fastapi
   ```

2. **Crear entorno virtual** (recomendado)
   ```bash
   python -m venv venv
   source venv/bin/activate  # En Windows: venv\Scripts\activate
   ```

3. **Instalar dependencias**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configurar variables de entorno**
   
   Crear archivo `.env` en la raíz del proyecto:
   ```env
   # Configuración de seguridad
   ALLOWED_DIRECTORIES=/ruta/permitida1,/ruta/permitida2
   MAX_FILE_SIZE=10485760  # 10MB en bytes
   ALLOWED_EXTENSIONS=.txt,.md,.py,.json,.csv,.log
   
   # Configuración del servidor
   HOST=127.0.0.1
   PORT=8000
   DEBUG=true
   ```

## 🚀 Uso

### Iniciar el servidor
```bash
uvicorn main:app --reload --host 127.0.0.1 --port 8000
```

### Configurar con Claude Desktop

Agregar la siguiente configuración al archivo de configuración de Claude Desktop:

```json
{
  "mcpServers": {
    "file-system": {
      "command": "uvicorn",
      "args": ["main:app", "--host", "127.0.0.1", "--port", "8000"],
      "cwd": "/ruta/al/proyecto/mcp_sistema_archivos_fastapi"
    }
  }
}
```

## 📚 API Endpoints

### Archivos

- **POST** `/archivos/crear` - Crear un nuevo archivo
- **GET** `/archivos/{ruta}` - Leer contenido de un archivo
- **PUT** `/archivos/{ruta}` - Actualizar contenido de un archivo
- **DELETE** `/archivos/{ruta}` - Eliminar un archivo
- **GET** `/archivos/buscar` - Buscar archivos por criterios

### Directorios

- **POST** `/directorios/crear` - Crear un nuevo directorio
- **GET** `/directorios/{ruta}` - Listar contenido de un directorio
- **DELETE** `/directorios/{ruta}` - Eliminar un directorio
- **GET** `/directorios/buscar` - Buscar directorios

### Metadatos

- **GET** `/metadatos/{ruta}` - Obtener información detallada de un archivo/directorio

## 🔒 Seguridad

### Características de seguridad implementadas:

- **Rutas restringidas**: Solo se permite acceso a directorios específicos configurados
- **Validación de rutas**: Prevención de path traversal attacks (../, ..\)
- **Límites de tamaño**: Restricciones en el tamaño máximo de archivos
- **Extensiones permitidas**: Lista blanca de extensiones de archivo permitidas
- **Sanitización de entrada**: Validación estricta de todos los parámetros de entrada

### Configuración de seguridad recomendada:

```env
# Limitar a directorios específicos seguros
ALLOWED_DIRECTORIES=/home/usuario/documentos,/home/usuario/proyectos

# Limitar tamaño de archivos (10MB)
MAX_FILE_SIZE=10485760

# Solo permitir extensiones seguras
ALLOWED_EXTENSIONS=.txt,.md,.py,.json,.csv,.log,.yaml,.yml
```

## 🧪 Pruebas

Ejecutar las pruebas unitarias:
```bash
python -m pytest pruebas/
```

Ejecutar pruebas con cobertura:
```bash
python -m pytest --cov=. pruebas/
```

## 📖 Documentación de la API

Una vez que el servidor esté ejecutándose, puedes acceder a:

- **Documentación interactiva (Swagger)**: http://127.0.0.1:8000/docs
- **Documentación alternativa (ReDoc)**: http://127.0.0.1:8000/redoc
- **Esquema OpenAPI**: http://127.0.0.1:8000/openapi.json

## 🔧 Desarrollo

### Arquitectura

Este proyecto sigue los principios de **Clean Architecture** y **SOLID**:

- **Separation of Concerns**: Cada capa tiene una responsabilidad específica
- **Dependency Inversion**: Las dependencias apuntan hacia abstracciones
- **Interface Segregation**: Interfaces específicas para cada funcionalidad
- **Single Responsibility**: Cada clase/módulo tiene una única responsabilidad

### Contribuir

1. Fork el proyecto
2. Crear una rama feature (`git checkout -b feature/nueva-funcionalidad`)
3. Commit los cambios (`git commit -am 'Agregar nueva funcionalidad'`)
4. Push a la rama (`git push origin feature/nueva-funcionalidad`)
5. Crear un Pull Request

## 📋 Requisitos del Sistema

- **Sistema Operativo**: Windows, macOS, Linux
- **Python**: 3.8 o superior
- **Memoria RAM**: Mínimo 512MB disponibles
- **Espacio en disco**: 100MB para instalación básica

## 🚨 Limitaciones y Consideraciones

- Las operaciones están limitadas a directorios configurados por seguridad
- El tamaño máximo de archivo está limitado por configuración
- No se permiten operaciones de sistema que puedan comprometer la seguridad
- Requiere configuración adecuada de permisos de sistema de archivos

## 🤝 Soporte

Si encuentras algún problema o tienes preguntas:

1. Revisa la documentación de la API en `/docs`
2. Consulta los logs del servidor para diagnóstico
3. Verifica la configuración de rutas permitidas
4. Crear un issue en GitHub con detalles del problema

## 📄 Licencia

Este proyecto está bajo la Licencia MIT. Ver el archivo `LICENSE` para más detalles.

---

🧑‍💻 **Desarrollado por**: Juan Esteban Valdés Ospina  
🏢 **Organización**: Agency CIC  
📧 **Contacto**: [GitHub Profile](https://github.com/juanesteban-valdesospina-agencycic)  

---

⭐ Si este proyecto te resulta útil, ¡no olvides darle una estrella en GitHub!