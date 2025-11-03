from datetime import datetime, timezone

# FastAPI 앱 시작 시각을 저장할 전역 변수
APP_START_TIME = datetime.now(timezone.utc).isoformat()