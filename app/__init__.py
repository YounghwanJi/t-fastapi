import importlib.metadata

try:
    __package_name__ = "my-fastapi-project"
    __version__ = importlib.metadata.version(__package_name__)
    __project_name__ = importlib.metadata.metadata(__package_name__)["name"]
except importlib.metadata.PackageNotFoundError:
    __version__ = "0.1.0(e)"
    __project_name__ = "My FastAPI Project(e)"

__author__ = "Your Name"
__email__ = "your.email@example.com"

__all__ = ["__version__", "__project_name__"]