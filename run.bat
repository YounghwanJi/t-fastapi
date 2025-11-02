@echo off
REM === Run FastAPI ===
REM Usage: run.bat [local|dev|qa|stg|prd]

setlocal

if "%~1"=="" (
    echo [ERROR] Choose your ENV. ex: run-env.bat dev
    exit /b 1
)

set ENV=%~1

if "%ENV%"=="local" (
    set ENV_FILE=.env.local
) else if "%ENV%"=="dev" (
    set ENV_FILE=.env.dev
) else if "%ENV%"=="qa" (
    set ENV_FILE=.env.qa
) else if "%ENV%"=="stg" (
    set ENV_FILE=.env.stg
) else if "%ENV%"=="prd" (
    set ENV_FILE=.env.prd
) else (
    echo [ERROR] Unkonwn environment: %ENV%
    exit /b 1
)

echo Starting FastAPI in %ENV% environment...
if "%ENV%"=="local" (
    uv run --env-file %ENV_FILE% uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload
) else (
    uv run --env-file %ENV_FILE% uvicorn app.main:app --host 0.0.0.0 --port 8000
)
