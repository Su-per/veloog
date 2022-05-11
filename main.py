from urllib.request import Request
from fastapi import FastAPI
from fastapi_versioning import VersionedFastAPI
import uvicorn
from loguru import logger
from routers import main_router, post_router


app = FastAPI(title="Veloog", description="Velog clone coding")
app.include_router(main_router.router)
app.include_router(post_router.router)


@app.middleware("http")
async def logging_middleware(request: Request, call_next):
    logger.info(f"{request.method} {request.url}")
    response = await call_next(request)
    logger.info(f"{response.status_code} {response.url}")
    return response


if __name__ == "__main__":
    app = VersionedFastAPI(
        app,
        version_format="{major}",
        prefix_format="/api/v{major}",
    )
    uvicorn.run(app, host="0.0.0.0", port=8000)
