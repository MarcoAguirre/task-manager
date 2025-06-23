# Task manage App
This is a backend app to manage tasks. It uses a CRUD to manage them

## Tech stack
- Python 3.11
- FastAPI
- SQLAlchemy
- SQLite
- Pydantic
- Docker
- Pytest
- flake8 / black

## Structure/Architecture

```
task-manager/
├── app/ # FastAPI app & routers
├── domain/ # Models and repositories
├── infrastructure/ # ORM and DB
├── usecases/
├── tests/
```

## How to run it
```bash
make install
make run

OR

docker compose up --build
```

## Run tests
```bash
make test
```

## Linters
```bash
make lint
make format
```