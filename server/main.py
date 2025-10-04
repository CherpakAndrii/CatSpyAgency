import uvicorn
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
from fastapi.middleware.gzip import GZipMiddleware
from contextlib import asynccontextmanager
# from filelock import FileLock, Timeout
import uvloop
import asyncio

from api.spy_cats_router import spy_cats_router
from api.missions_router import missions_router
from api.targets_router import targets_router
from constants import SERVER_PORT, SERVER_WORKERS
from utils.launch_utils import configure_logging, configure_directories


asyncio.set_event_loop_policy(uvloop.EventLoopPolicy())

@asynccontextmanager
async def lifespan(application: FastAPI):
    # Perform startup tasks
    configure_logging()

    # lock = FileLock("startup.lock")
    # try:
    #     with lock.acquire(timeout=0):
    #         configure_directories()
    # except Timeout:
    #     pass
    yield
    # Perform shutdown tasks

app = FastAPI(lifespan=lifespan)

origins = [
    "http://localhost:3000",
    "http://192.168.0.101:3000",
    "http://localhost:8000",
    "http://192.168.0.101:8000",
    # TODO add your origins here
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.add_middleware(GZipMiddleware, minimum_size=4096)

app.include_router(spy_cats_router, prefix="/api/cats", tags=["SpyCats"])
app.include_router(missions_router, prefix="/api/missions", tags=["Missions"])
app.include_router(targets_router, prefix="/api/targets", tags=["Targets"])


if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=SERVER_PORT, workers=SERVER_WORKERS)
