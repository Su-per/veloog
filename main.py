from fastapi import FastAPI
from fastapi_versioning import VersionedFastAPI
from routers import main_router
app = FastAPI(
    title="Veloog",
    description="Veloog clone coding"
)
app.include_router(main_router.router)


if __name__ == '__main__':
    import uvicorn
    app = VersionedFastAPI(app, version_format = "{major}", prefix_format = "/api/v{major}",)
    uvicorn.run(app, host='0.0.0.0', port=8000)
    