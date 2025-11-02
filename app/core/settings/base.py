from pydantic_settings import BaseSettings
from typing import List
from app import __version__, __project_name__

class BaseConfig(BaseSettings):
    """모든 환경의 공통 설정"""
    PROJECT_NAME: str = __project_name__
    VERSION: str = __version__