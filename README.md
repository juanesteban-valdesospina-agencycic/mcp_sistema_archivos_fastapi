# 🗂️ MCP Sistema de Archivos FastAPI

Un servidor **Model Context Protocol (MCP)** construido con FastAPI que permite a sistemas de IA y usuarios interactuar de forma segura con el sistema de archivos local a través de operaciones REST y MCP.

## 📦 ¿Qué es este proyecto?

Este proyecto implementa un servidor MCP que expone operaciones seguras de gestión de archivos y directorios, pensado para integraciones con asistentes de IA (Claude, Copilot, Cursor, etc.) y automatización de tareas de desarrollo.

## ✨ Características

- 🔒 Operaciones seguras y restringidas a directorios autorizados
- 📂 CRUD completo de archivos y directorios
- 🔍 Búsqueda de archivos por nombre, extensión o patrón
- 📊 Metadatos detallados de archivos
- 🏗️ Arquitectura limpia y modular (Clean Architecture)
- 🔌 Integración nativa con MCP y FastAPI
- 📋 Validación robusta de rutas y entradas

## 📁 Estructura del Proyecto

```
mcp_sistema_archivos/
├── main.py                  # Punto de entrada FastAPI + MCP
├── dependencias.py          # Inyección de dependencias
├── enrutadores/             # Routers para endpoints REST
│   ├── crear.py
│   ├── obtener.py
│   ├── actualizar.py
│   └── eliminar.py
├── servicios/               # Lógica de negocio
│   ├── crear.py
│   ├── obtener.py
│   ├── eliminar.py
│   └── interfaces/          # Interfaces (contratos ABC)
│       ├── crear.py
│       ├── obtener.py
│       └── eliminar.py
├── esquemas/                # Esquemas Pydantic (DTOs)
│   └── dtos.py
├── pruebas/                 # Tests unitarios y de integración
│   ├── integracion/
│   └── unitarias/
└── requirements.txt         # Dependencias
```

## 🚀 Instalación y Configuración

### Prerrequisitos
- Python 3.8 o superior
- pip

### Pasos

1. **Clona el repositorio**
   ```bash
   git clone https://github.com/juanesteban-valdesospina-agencycic/mcp_sistema_archivos_fastapi.git
   cd mcp_sistema_archivos_fastapi
   ```
2. **Crea un entorno virtual**
   ```bash
   python -m venv venv
   source venv/bin/activate  # En Windows: venv\Scripts\activate
   ```
3. **Instala dependencias**
   ```bash
   pip install -r requirements.txt
   ```
4. **Configura variables de entorno**
   Crea un archivo `.env` en la raíz:
   ```env
   # Carpeta raíz permitida para operaciones
   CARPETA_RAIZ_PROYECTOS=/Users/jevdev2304/Documents/CIC
   # Configuración del servidor
   HOST=0.0.0.0
   PORT=8000
   DEBUG=true
   ```

## 🎮 Uso

### Iniciar el servidor
```bash
uvicorn main:app --host 0.0.0.0 --port 8000 --reload
```

## 🔌 Configuración MCP

Ejemplo para `settings.json` de Claude Desktop o Cursor:
```json
{
  "mcpServers": {
    "file-system": {
      "command": "uvicorn",
      "args": ["main:app", "--host", "0.0.0.0", "--port", "8000"],
      "cwd": "/ruta/al/proyecto/mcp_sistema_archivos"
    }
  }
}
```

## 📚 Endpoints REST Principales

### Archivos
- **GET** `/obtener/archivos/{ruta:path}` - Leer archivo
- **POST** `/crear/archivo` - Crear o sobrescribir archivo (texto o upload)
- **PUT** `/actualizar/archivo` - Actualizar archivo existente
- **DELETE** `/eliminar/archivo` - Eliminar archivo
- **GET** `/obtener/buscar` - Buscar archivos por patrón

### Directorios
- **GET** `/obtener/carpeta` - Listar contenido de un directorio
- **POST** `/crear/carpeta` - Crear nuevo directorio
- **DELETE** `/eliminar/carpeta` - Eliminar directorio

### Metadatos
- **GET** `/obtener/metadatos` - Obtener información detallada de archivo/directorio

## 🔒 Seguridad

- Todas las rutas se validan para evitar path traversal y acceso fuera de la carpeta raíz
- Solo se permiten operaciones dentro de `CARPETA_RAIZ_PROYECTOS`
- Validación estricta de parámetros y extensiones
- Manejo robusto de errores y respuestas HTTP

## 🧪 Pruebas

Ejecuta los tests unitarios y de integración:
```bash
python -m pytest pruebas/
```

## 🛠️ Arquitectura

- **Clean Architecture**: separación de routers, servicios, interfaces y esquemas
- **Interfaces**: implementadas como ABCs en `servicios/interfaces/`
- **Servicios**: lógica de negocio desacoplada de FastAPI
- **Routers**: definen los endpoints REST y delegan en servicios

## 🤝 Contribución

1. Haz fork del repo
2. Crea una rama feature (`git checkout -b feature/nueva-funcionalidad`)
3. Implementa cambios siguiendo la arquitectura existente
4. Agrega tests para nuevas funcionalidades
5. Haz commit y push
6. Crea un Pull Request

## 📞 Soporte y Contacto

- **Desarrollador**: Juan Esteban Valdés Ospina
- **Organización**: Agency CIC
- **GitHub**: [@juanesteban-valdesospina-agencycic](https://github.com/juanesteban-valdesospina-agencycic)
- **Email**: juan.valdes@agencycic.com

---

⭐ Si este proyecto te resulta útil, ¡dale una estrella en GitHub!