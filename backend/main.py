from fastapi import FastAPI
from routes.actors import router as actors_router

app = FastAPI(
    title="Hollywood Actors API",
    version="1.0.0"
)

app.include_router(actors_router)
