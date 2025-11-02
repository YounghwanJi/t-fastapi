local:
    uv run --env-file .env.local uvicorn app.main:app --host 0.0.0.0 --reload
dev:
    uv run --env-file .env.dev uvicorn app.main:app --host 0.0.0.0
qa:
    uv run --env-file .env.qa uvicorn app.main:app --host 0.0.0.0
stg:
    uv run --env-file .env.stg uvicorn app.main:app --host 0.0.0.0
prd:
    uv run --env-file .env.prd uvicorn app.main:app --host 0.0.0.0