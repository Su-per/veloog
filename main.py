from fastapi import FastAPI
from fastapi_versioning import VersionedFastAPI

app = FastAPI()


if __name__ == '__main__':
    import uvicorn
    app = VersionedFastAPI(app, version_format="{major}", prefix_format="/api/v{major}")
    uvicorn.run(app, host="0.0.0.0", port=8000)
