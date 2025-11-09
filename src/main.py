from contextlib import asynccontextmanager
from fastapi import FastAPI

from .core.config import settings
from .core.database import Base, engine
from . import models
from .graphql.router import graphql_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    """
    Application lifespan: initialize database tables at startup.
    Ensures all SQLAlchemy models are imported so Base.metadata is complete,
    then creates missing tables.
    """

    Base.metadata.create_all(bind=engine)
    yield


app = FastAPI(
    lifespan=lifespan,
    title=settings.APP_NAME,
    version=settings.APP_VERSION,
)

app.include_router(graphql_router, prefix="/graphql")


@app.get("/")
async def root():
    """Root endpoint returning a welcome message."""
    return {
        "message": f"Welcome to {settings.APP_NAME}",
        "graphql": "/graphql",
    }


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(
        app,
        host=settings.HOST,
        port=int(settings.PORT),
    )
