from app.core.settings.base import BaseConfig

class DevConfig(BaseConfig):

    class Config:
        env_file = ".env.dev"
        env_file_encoding = "utf-8"