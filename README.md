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
|   ├──interfaces/            #Definición de interfaces (abstracción de la lógica de negocio)
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

![image](https://github.com/user-attachments/assets/70703ec4-bf78-4328-b0f0-68e03fc607a1)


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
Contienen interfaces (contratos) que definen los métodos necesarios para cada Servicio.

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

Finalmente, se diseño esta plantilla modular para FastAPI siguiendo los principios de diseño SOLID y con una estructura inspirada en el Domain-Driven Design (DDD), una filosofía de desarrollo que propone modelar el software en torno al dominio del negocio, organizando el código por capas como entidades, servicios, repositorios e interfaces. Esto me permitió garantizar un código limpio, flexible y fácil de mantener. La clara separación de responsabilidades, el uso de interfaces específicas y la inyección de dependencias aseguran que el sistema sea escalable y desacoplado. Además, esta arquitectura facilita la creación de pruebas unitarias, ya que permite usar implementaciones falsas (mocks o fakes) para aislar la lógica de negocio y probar cada componente de forma independiente. En la carpeta llamada pruebas se incluyen dos ejemplos: uno con tres pruebas unitarias y otro con una prueba de integración contra la base de datos. Entiendo que actualmente puede que no se realicen pruebas, pero si en un futuro la compañía decide implementarlas, estos ejemplos sirven como evidencia de que esta arquitectura permite hacerlo sin problemas. Esto no solo mejora la calidad del código, sino que también acelera el desarrollo y reduce riesgos en futuros cambios.

🧑‍💻 Autor
Desarrollado por Juan Esteban Valdés Ospina ✨
