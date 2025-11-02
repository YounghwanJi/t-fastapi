from app.core.settings.base import BaseConfig

class PrdConfig(BaseConfig):

    class Config:
        env_file = ".env.prd"
        env_file_encoding = "utf-8"