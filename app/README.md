# sample-api-app



## Local development

To install project dependencies for development, use poetry:

```
poetry install --with=development
```

You must have `.env` file with correct content in the app root directory in order to correctly start the application. `.env.example` is an example configuration file.

To start local development server, run following:

```
PYTHONPATH=src poetry run python3 src/entrypoints/asgi_dev.py
```

The same file exports asgi-compatible object named `app`, so uvicorn can import it from this entrypoint. 

## Application server run

Do not use development server in production version. Use at least externally created uvicorn process that imports `entrypoints/asgi.py::app`.

To start a basic uvicorn application server use

```
cd src/entrypoints
PYTHONPATH=.. poetry run uvicorn "asgi:app"
```