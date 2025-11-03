from fastapi import APIRouter
from app.api.root.endpoints import root_endpoints

router = APIRouter()

router.include_router(root_endpoints.router)
