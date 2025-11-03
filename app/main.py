import logging
from fastapi import FastAPI
from app.core.config import settings
from app.core.state import APP_START_TIME
from app.api.root import root_router as api_router_root


logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",  # 포맷
)

app = FastAPI(
    title=settings.PROJECT_NAME,
    version=settings.VERSION,
)

app.include_router(api_router_root.router, prefix="")

@app.get("/")
async def root():
    return {"message": f"project: {settings.PROJECT_NAME}\nversion: {settings.VERSION}"}
