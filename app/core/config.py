import os
from functools import lru_cache
from app.core.settings.base import BaseConfig
from app.core.settings.local import LocalConfig
from app.core.settings.qa import QaConfig
from app.core.settings.stg import StgConfig
from app.core.settings.prd import PrdConfig

# 환경 설정 매핑
config_map: dict[str, type[BaseConfig]] = {
    "local": LocalConfig,
    "qa": QaConfig,
    "stg": StgConfig,
    "prd": PrdConfig,
}

@lru_cache()
def get_settings() -> BaseConfig:
    """환경에 맞는 설정 반환"""
    env = os.getenv("ENV", "local").lower()
    config_class = config_map.get(env, LocalConfig)
    return config_class()

# 전역 설정 객체
settings = get_settings()