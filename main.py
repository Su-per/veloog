from fastapi import FastAPI


from core.config import settings


app = FastAPI(title=settings.PROJECT_NAME)


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
