from app.core.settings.base import BaseConfig

class StgConfig(BaseConfig):

    class Config:
        env_file = ".env.stg"
        env_file_encoding = "utf-8"