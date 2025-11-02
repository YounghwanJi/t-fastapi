from app.core.settings.base import BaseConfig

class QaConfig(BaseConfig):

    class Config:
        env_file = ".env.qa"
        env_file_encoding = "utf-8"