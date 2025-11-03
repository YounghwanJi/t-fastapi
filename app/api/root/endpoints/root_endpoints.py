from fastapi import APIRouter
from fastapi.responses import JSONResponse
from datetime import datetime, timezone
from git import Repo, InvalidGitRepositoryError
from app.core.config import settings
from app.core.state import APP_START_TIME

router = APIRouter()

# ===================================================================
# ROUTERS
# ===================================================================

@router.get("/health", summary="Health check", tags=["Root"])
def health_check():
    return JSONResponse(content={"status": "UP"}, status_code=200)

@router.get("/info", summary="Application information", tags=["Root"])
def info():
    info_data = {
        "git": get_git_info(),
        "build": get_build_info(),
    }

    return JSONResponse(content=info_data, status_code=200)

# ===================================================================
# FUNCTIONS
# ===================================================================

def get_build_info() -> dict:
    """
    settings에서 name, version 정보를 읽어 build 정보 구성
    """

    return {
        "name": settings.PROJECT_NAME,
        "version": settings.VERSION,
        "time": APP_START_TIME,
    }


def get_git_info() -> dict:
    """
    현재 Git repository에서 branch, commit id, commit time 추출
    """
    try:
        repo = Repo(search_parent_directories=True)
        branch = repo.active_branch.name if not repo.head.is_detached else "DETACHED"
        commit = repo.head.commit
        commit_id = commit.hexsha[:7]
        commit_time = datetime.fromtimestamp(commit.committed_date, tz=timezone.utc).isoformat()
        return {
            "branch": branch,
            "commit": {"id": commit_id, "time": commit_time},
        }
    except InvalidGitRepositoryError:
        # git repo가 아니거나 .git 폴더가 없는 경우 fallback
        return {
            "branch": "unknown",
            "commit": {"id": "unknown", "time": None},
        }