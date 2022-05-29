from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from core.config import settings


app = FastAPI(title=settings.PROJECT_NAME)


if __name__ == "__main__":
    pass
