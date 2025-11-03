# Init
- Python 3.10
- FASTAPI
- UV
- Dependency
  - uvicorn[standard]


# Installation ( Do not run these commands. Instead, use ```uv sync```.)
``` bash
$ uv init
$ uv add fastapi
$ uv add "uvicorn[standard]"
$ uv add pydantic
$ uv add pydantic-settings
$ uv add gitpython
```

# Do this
``` bash
#  for use importlib.metadata (This command is also included in setup.sh.)
project_root $ uv pip install -e .
```


# Run
``` bash
# Windows
\> .\run.bat ${ENV}
# Ubuntu
$ make ${ENV}

# ${ENV}: local|dev|qa|stg|prd
```