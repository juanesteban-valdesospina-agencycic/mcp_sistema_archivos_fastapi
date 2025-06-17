# ⚙️ FastAPI Plantilla Modular
Este proyecto es una plantilla base para backend con FastAPI, diseñada con una arquitectura limpia, modular y desacoplada. No se utiliza un ORM, pero se siguen principios que facilitan el mantenimiento, escalabilidad y testeo del sistema.

## 📁 Estructura del Proyecto
```
fast_api_plantilla/
├── main.py                   # Punto de entrada de la aplicación
├── repositorios/
│   ├── interfaces/           # Definición de interfaces (abstracción del acceso a datos)
│   └── *.py                  # Implementación concreta de cada repositorio por entidad
├── servicios/
│   └── *.py                  # Lógica de negocio de cada entidad
├── modelos/
│   └── *.py                  # Definición de entidades (espejo de las tablas de BD, sin ORM)
├── esquemas/
│   └── *.py                  # DTOs (schemas de entrada/salida) por entidad
├── enrutadores/
│   └── *.py                  # Routers (capa de presentación) con inyección de dependencias
├── dependencias.py           # Registro de servicios e inyección mediante Depends()
├── db.py                     # Lógica para obtener conexión a la base de datos
├── .env                      # Variables de entorno (credenciales, configuración)
├── .gitignore
```
## 🧠 Arquitectura y Conocimientos Técnicos Aplicados
### ✅ main.py
Archivo raíz del proyecto.

Crea la instancia FastAPI.

Registra los routers de la capa de presentación.

### ✅ repositorios/
Contienen interfaces (contratos) que definen los métodos necesarios para cada entidad.

Cada implementación concreta gestiona directamente la conexión a la base de datos (extracción, inserción, etc.).

Aplica el principio de inversión de dependencias (Dependency Inversion).

### ✅ servicios/
Implementan la lógica de negocio de cada entidad.

Consumidos por los routers mediante inyección de dependencias.

Separan reglas del negocio del acceso a datos y de la presentación.

### ✅ modelos/
Representan las entidades del sistema.

Aunque no se usa ORM, sirven como un espejo de las tablas de la base de datos para mantener el código organizado y coherente.

### ✅ esquemas/
Cada entidad tiene su archivo .py correspondiente.

Se definen los esquemas de entrada y salida utilizando Pydantic.

Facilitan validación automática y documentación de la API.

### ✅ dependencias.py
Centraliza la lógica de inyección de dependencias.

Define cómo obtener instancias de servicios y repositorios usando Depends() de FastAPI.

### ✅ enrutadores/
Exponen las rutas de la API organizadas por entidad.

Se inyectan los servicios necesarios desde dependencias.py con Depends().

### ✅ db.py
Lógica de conexión a base de datos (MySQL o similar).

Devuelve la conexión y cursor necesarios para ejecutar consultas sin ORM.

## 🔐 Variables de entorno (.env)
Ejemplo:

DB_HOST=localhost  
DB_USER=usuario  
DB_PASSWORD=contraseña  
DB_NAME=nombre_basedatos

## ▶️ Ejecutar el proyecto
Instalar dependencias:

pip install -r requirements.txt
Iniciar servidor:


uvicorn main:app --reload

## 🎯 Beneficios de esta arquitectura
Separación clara de responsabilidades (repositorios, servicios, presentación).

Facilita pruebas unitarias al tener lógica desacoplada.

Escalable: se pueden añadir nuevas entidades fácilmente.

Uso de interfaces fomenta el principio de programación orientada a contratos.

🧑‍💻 Autor
Desarrollado por Juan Esteban Valdés Ospina ✨
