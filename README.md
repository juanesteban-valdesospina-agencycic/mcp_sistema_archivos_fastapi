# 🗂️ MCP Sistema de Archivos FastAPI

Un servidor **Model Context Protocol (MCP)** especializado en gestión de archivos, construido con FastAPI que permite a sistemas de IA interactuar de forma segura con el sistema de archivos local a través de operaciones REST.

## 🎯 ¿Qué es este proyecto?

Este proyecto implementa un **servidor MCP (Model Context Protocol)** que proporciona una interfaz segura y controlada para que la IA pueda realizar operaciones de gestión de archivos y directorios. Está diseñado específicamente para automatizar tareas de desarrollo y facilitar la integración con herramientas de IA como asistentes de código.

### 🔗 ¿Qué es MCP?

**Model Context Protocol (MCP)** es un protocolo estándar que permite a los modelos de IA acceder a recursos externos de manera segura. Este servidor proporciona acceso controlado al sistema de archivos local, permitiendo que la IA pueda leer, crear, modificar y eliminar archivos dentro de carpetas específicas autorizadas.

## ✨ Características Principales

- 🔒 **Seguridad por diseño**: Operaciones limitadas a directorios específicos con validación de rutas
- 📂 **Gestión completa de archivos**: Crear, leer y eliminar archivos y directorios
- 🌳 **Exploración de proyectos**: Listado y navegación de estructuras de directorios
- 📊 **Múltiples formatos**: Soporte para subida de archivos y creación desde texto plano
- 🏗️ **Arquitectura limpia**: Clean Architecture con interfaces y servicios separados
- 🔌 **Integración MCP nativa**: Compatible con FastApiMCP para exposición automática
- ⚡ **Alto rendimiento**: Construido con FastAPI para máxima velocidad
- 🎨 **API REST moderna**: Endpoints RESTful con documentación automática

## 📁 Estructura del Proyecto

```
mcp_sistema_archivos_fastapi/
├── main.py                     # Punto de entrada con integración MCP
├── dependencias.py             # Inyección de dependencias para servicios
├── enrutadores/
│   ├── obtener.py             # Endpoints para leer archivos y explorar directorios
│   ├── crear.py               # Endpoints para crear archivos (upload/texto)
│   └── eliminar.py            # Endpoints para eliminar archivos/directorios
├── servicios/
│   ├── interfaces/            # Interfaces de servicios (contratos)
│   │   ├── obtener.py         # IServicioObtener
│   │   ├── crear.py           # IServicioCrear
│   │   └── eliminar.py        # IServicioEliminar
│   ├── obtener.py             # Lógica para exploración y lectura
│   ├── crear.py               # Lógica para creación de archivos
│   └── eliminar.py            # Lógica para eliminación segura
└── requirements.txt           # Dependencias del proyecto
```

## 🚀 Instalación y Configuración

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
   # Configuración de carpeta raíz de proyectos
   CARPETA_RAIZ_PROYECTOS=/Users/jevdev2304/Documents/CIC
   
   # Configuración del servidor
   HOST=0.0.0.0
   PORT=8000
   DEBUG=true
   ```

## 🎮 Uso

### Iniciar el servidor
```bash
python main.py
```

O usando uvicorn directamente:
```bash
uvicorn main:app --host 0.0.0.0 --port 8000 --reload
```

### Configurar con Claude Desktop

Agregar la siguiente configuración al archivo de configuración de Claude Desktop:

```json
{
  "mcpServers": {
    "file-system": {
      "command": "python",
      "args": ["/ruta/completa/al/proyecto/main.py"],
      "cwd": "/ruta/al/proyecto/mcp_sistema_archivos_fastapi"
    }
  }
}
```

## 📚 API Endpoints

### 🔍 Obtener - Exploración y Lectura

- **GET** `/obtener/proyectos` - Lista todos los proyectos en la carpeta raíz
  - **Operation ID:** `get_projects`
  - **Descripción:** Obtiene un listado de todos los directorios proyecto disponibles

- **GET** `/obtener/carpeta` - Explora contenido de una carpeta específica
  - **Operation ID:** `get_folder_content`  
  - **Parámetros:** `ruta_carpeta` (query parameter)
  - **Descripción:** Lista archivos y subdirectorios de la carpeta especificada

- **GET** `/obtener/archivos/{archivo:path}` - Lee contenido de un archivo
  - **Operation ID:** `read_file`
  - **Parámetros:** `archivo` (path parameter)
  - **Descripción:** Retorna el contenido completo del archivo especificado

### ✏️ Crear - Creación de Archivos

- **POST** `/crear/archivo/upload` - Subida de archivos
  - **Operation ID:** `create_or_overwrite_file_using_upload`
  - **Parámetros:** 
    - `carpeta_destino` (form field)
    - `archivo` (file upload)
  - **Descripción:** Crea o sobrescribe un archivo mediante upload

- **POST** `/crear/archivo/texto` - Creación desde texto plano
  - **Operation ID:** `create_or_overwrite_file_using_text`
  - **Body:** `{"carpeta_destino": "ruta", "nombre_archivo": "nombre", "contenido": "texto"}`
  - **Descripción:** Crea o sobrescribe un archivo desde contenido de texto

### 🗑️ Eliminar - Eliminación Segura

- **DELETE** `/eliminar/archivo` - Elimina archivos o directorios
  - **Operation ID:** `delete_file`
  - **Parámetros:** `ruta_objetivo` (form field)
  - **Descripción:** Elimina de forma segura archivos o directorios completos

## 🔒 Características de Seguridad

### Validaciones Implementadas:

- **🛡️ Restricción de rutas**: Solo permite operaciones dentro de `CARPETA_RAIZ_PROYECTOS`
- **🔍 Validación de path traversal**: Previene acceso fuera de directorios autorizados
- **📁 Verificación de existencia**: Valida que carpetas destino existan antes de operar
- **⚠️ Manejo de errores**: Respuestas HTTP apropiadas para diferentes tipos de error

### Configuración de seguridad:

```python
# Las rutas se resuelven relativamente a la carpeta base
ruta_base = Path(os.getenv("CARPETA_RAIZ_PROYECTOS", "/Users/jevdev2304/Documents/CIC"))

# Validación: la ruta objetivo debe estar dentro de la ruta base
try:
    objetivo.relative_to(ruta_base)
except ValueError:
    raise HTTPException(status_code=403, detail="Acceso denegado")
```

## 🧪 Casos de Uso

### 🤖 Automatización con IA

- **Análisis de código**: La IA puede leer archivos de proyecto para entender el contexto
- **Generación de documentación**: Crear archivos README, documentación técnica automáticamente
- **Refactoring asistido**: Modificar múltiples archivos siguiendo patrones específicos
- **Gestión de configuración**: Crear/actualizar archivos de configuración de proyectos
- **Backup selectivo**: Crear copias de archivos importantes basándose en criterios

### 💼 Desarrollo de Software

- **Exploración de proyectos**: Navegar rápidamente por estructuras de directorios complejas
- **Gestión de templates**: Crear archivos base desde plantillas predefinidas
- **Sincronización**: Mantener archivos sincronizados entre diferentes entornos
- **Auditoría de código**: Revisar y documentar cambios en archivos fuente

## 📖 Documentación de la API

Una vez que el servidor esté ejecutándose, puedes acceder a:

- **📋 Documentación interactiva (Swagger)**: http://localhost:8000/docs
- **📚 Documentación alternativa (ReDoc)**: http://localhost:8000/redoc  
- **🔧 Esquema OpenAPI**: http://localhost:8000/openapi.json

## 🔧 Arquitectura Técnica

### Principios de Diseño

Este proyecto implementa **Clean Architecture** con los siguientes principios:

- **🏗️ Separation of Concerns**: Cada capa tiene responsabilidades específicas
- **🔄 Dependency Inversion**: Servicios dependen de interfaces, no implementaciones
- **📋 Interface Segregation**: Interfaces específicas para cada funcionalidad  
- **🎯 Single Responsibility**: Cada clase/módulo tiene una única responsabilidad

### Flujo de Datos

```
Cliente MCP → FastAPI → Enrutadores → Servicios → Sistema de Archivos
     ↓              ↓          ↓           ↓              ↓
  Solicitud → Validación → Lógica → Operación → Respuesta
```

### Servicios Implementados

1. **ServicioObtener**: Maneja lectura y exploración
   - `obtener_proyectos()`: Lista directorios proyecto
   - `obtener_contenido_carpeta()`: Explora carpetas específicas  
   - `leer_archivo()`: Lee contenido de archivos
   - `obtener_estructura_completa_texto()`: Genera árbol JSON completo

2. **ServicioCrear**: Maneja creación de archivos
   - `crear_o_sobrescribir_archivo()`: Upload de archivos
   - `crear_o_sobrescribir_archivo_texto()`: Creación desde texto

3. **ServicioEliminar**: Maneja eliminación segura
   - `eliminar()`: Elimina archivos y directorios

## 🚨 Limitaciones y Consideraciones

### Limitaciones Actuales:
- ⚠️ **Rutas hardcodeadas**: La carpeta base está configurada específicamente
- 📁 **Sin autenticación**: No implementa sistema de usuarios/permisos
- 💾 **Sin límites de tamaño**: No hay restricciones en tamaño de archivos
- 🔍 **Sin búsqueda avanzada**: Búsqueda limitada a navegación directa

### Próximas Mejoras:
- 🌐 **Configuración flexible**: Variables de entorno para múltiples proyectos
- 🔐 **Sistema de autenticación**: Tokens de acceso y permisos granulares
- 📊 **Límites de recursos**: Restricciones de tamaño y velocidad
- 🔍 **Búsqueda avanzada**: Búsqueda por contenido, extensión, fecha
- 📝 **Logging completo**: Registro detallado de todas las operaciones

## 🤝 Desarrollo y Contribución

### Para contribuir:

1. Fork el proyecto
2. Crear rama feature (`git checkout -b feature/nueva-funcionalidad`)
3. Implementar cambios siguiendo la arquitectura existente
4. Agregar tests para nuevas funcionalidades
5. Commit cambios (`git commit -am 'Agregar nueva funcionalidad'`)
6. Push a la rama (`git push origin feature/nueva-funcionalidad`)
7. Crear Pull Request

### Estructura para nuevas funcionalidades:

1. **Interface** en `servicios/interfaces/`
2. **Implementación** en `servicios/`
3. **Enrutador** en `enrutadores/`
4. **Registrar dependencia** en `dependencias.py`
5. **Incluir router** en `main.py`

## 📋 Estado del Proyecto

### ✅ Implementado (Julio 2025)
- ✅ Servicios core de obtener, crear y eliminar
- ✅ API REST completa con 6 endpoints
- ✅ Integración MCP con FastApiMCP
- ✅ Validaciones de seguridad básicas
- ✅ Arquitectura limpia con interfaces

### 🔄 En desarrollo
- 🔧 Instalación en servidor de desarrollo
- 🌐 Exposición para clientes IA externos
- 📚 Documentación completa de casos de uso
- ⚡ Optimizaciones de rendimiento

### 📝 Roadmap
- 🔐 Sistema de autenticación y autorización
- 🔍 Funcionalidades de búsqueda avanzada
- 📊 Métricas y monitoreo
- 🧪 Suite completa de tests
- 📦 Empaquetado para distribución

## 📞 Soporte y Contacto

### 🐛 Reportar problemas:
1. Revisar documentación en `/docs`
2. Verificar logs del servidor
3. Comprobar configuración de variables de entorno
4. Crear issue en GitHub con detalles completos

### 📧 Contacto:
- **👨‍💻 Desarrollador**: Juan Esteban Valdés Ospina
- **🏢 Organización**: Agency CIC  
- **🐙 GitHub**: [@juanesteban-valdesospina-agencycic](https://github.com/juanesteban-valdesospina-agencycic)
- **📧 Email**: juan.valdes@agencycic.com

---

## 📄 Licencia

Este proyecto está bajo la Licencia MIT. Ver el archivo `LICENSE` para más detalles.

---

⭐ **¡Si este proyecto te resulta útil, no olvides darle una estrella en GitHub!** ⭐

*Última actualización: 10 de julio de 2025*