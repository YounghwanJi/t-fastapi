from fastapi import FastAPI
from app.core.config import settings

app = FastAPI(
    title=settings.PROJECT_NAME,
    version=settings.VERSION,
)

@app.get("/")
async def root():
    return {"message": f"project: {settings.PROJECT_NAME}\nversion: {settings.VERSION}"}
