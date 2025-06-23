## Requerimientos iniciales
Para facilitar la instalación de dependencias, decidí crear un archivo requirements.txt desde el inicio. Esto permite a cualquier persona clonar el proyecto y ejecutar un único comando para tener todas las dependencias listas (pip install -r requirements.txt).

## Estructura base y contenedor
El primer paso fue establecer un punto de entrada básico para la aplicación, junto con todos los archivos que necesitaría más adelante aunque estén vacíos.

## Diseño de modelos y arquitectura
Separé los modelos de dominio (Task, TaskList) del resto del sistema para mantener una arquitectura limpia y coherente con principios de diseño como Hexagonal/Clean Architecture.

## Repositorios
Usé interfaces en domain/repositories para definir los métodos necesarios sin acoplarme a ninguna tecnología. Luego implementé esas interfaces en infrastructure/repositories usando SQLAlchemy.

Este patrón me permite no depender de una base de datos específica.

## Usecases
Cada acción importante (crear, actualizar, eliminar) se encapsula en un usecase, lo cual permite mantener una lógica reutilizable, clara y testeable.

## Endpoints
Una vez que todo el backend interno estuvo listo (modelos, repositorios, usecases), conecté esa lógica a través de endpoints con FastAPI.

## Dockerización
El proyecto incluye un Dockerfile y un docker-compose.yml para que se pueda correr en cualquier entorno. Esto elimina la necesidad de instalar Python, paquetes o configurar el entorno manualmente.

## Makefile y herramientas de desarrollo
Para facilitar la ejecución de comandos, agregué un Makefile con tareas como:
```
make run → correr la app sin Docker

make test → ejecutar tests

make lint → revisar estilo con flake8

make format → formatear con black
```

También agregué flake8 y black para asegurar un código limpio, legible y estandarizado.

## Testing
Al final del proyecto, agregué pruebas unitarias para todos los usecases principales. Esto permite validar el comportamiento de la lógica sin depender de una base de datos real.

## Resultado
El proyecto ahora:

- Sigue una arquitectura hexagonal

- Es portable (Docker)

- Está cubierto por pruebas aunque puede tener mas casos de test

- Puede ser ejecutado por cualquier persona únicamente con docker