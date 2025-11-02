from app.core.settings.base import BaseConfig

class LocalConfig(BaseConfig):

    class Config:
        env_file = ".env.local"
        env_file_encoding = "utf-8"