from fastapi import FastAPI
from fastapi_versioning import VersionedFastAPI
import uvicorn
from routers import main_router, post_router
app = FastAPI(
    title="Veloog",
    description="Veloog clone coding"
)
app.include_router(main_router.router)
app.include_router(post_router.router)


if __name__ == '__main__':
    import os
    app = VersionedFastAPI(app, version_format = "{major}", prefix_format = "/api/v{major}",)
    uvicorn.run(app, host="0.0.0.0", port=8000)