# service-controller-notebookum

Controlador de llamadas / API Gateway para el ecosistema NotebookUm.

Este microservicio actúa como un orquestador central que recibe solicitudes externas, enruta y coordina llamadas hacia los servicios de NotebookUm.

## Características

- API basada en FastAPI
- Healthcheck básico
- Lectura de configuración desde variables de entorno
- Contenedor Docker listo para desarrollo y despliegue
- Configuración de ejemplo en `.env.example`

## Estructura del proyecto

- `main.py`: punto de entrada del servicio
- `app/__init__.py`: paquete principal
- `app/config.py`: configuración del servicio
- `pyproject.toml`: dependencias y metadatos del proyecto
- `.env.example`: plantilla de variables de entorno
- `Dockerfile`: construcción de imagen Docker
- `docker-compose.yml`: configuración local con Docker Compose

## Requisitos

- Python 3.11 o superior
- pip
- Docker (opcional, para contenedores)

## Configuración local

1. Copia el archivo de ejemplo:
   ```bash
   copy .env.example .env
   ```
2. Ajusta las variables de entorno en `.env` según tu entorno.

## Instalación

```bash
python -m venv .venv
.\.venv\Scripts\activate
pip install --upgrade pip
pip install -r requirements.txt
```

> Si prefieres usar `pyproject.toml`, instala con:

```bash
pip install .
```

## Ejecución

### Con Uvicorn

```bash
uvicorn main:app --host 0.0.0.0 --port 8000
```

### Con Docker

```bash
docker build -t notebookum-controller .
docker run --env-file .env.example -p 8000:8000 notebookum-controller
```

### Con Docker Compose

```bash
docker compose up --build
```

## Endpoints principales

- `GET /healthz` — verificación de estado
- `GET /orchestrate` — endpoint de prueba de orquestación

## Variables de entorno

- `FASTAPI_HOST` — Host donde escucha el servidor
- `FASTAPI_PORT` — Puerto del servidor
- `NOTEBOOKUM_SERVICE_URL` — URL base del servicio NotebookUm
- `LOG_LEVEL` — Nivel de logs
- `PYTHONUNBUFFERED` — Controla salida sin buffer

## Desarrollo

- Mantener la configuración en `.env`
- No subir archivos `.env` reales al repositorio
- Usar `.env.example` como plantilla para otros desarrolladores

## Contribuciones

1. Abrir un issue describiendo la mejora
2. Crear una rama temática
3. Enviar un pull request con tests cuando aplique

## Licencia

MIT
