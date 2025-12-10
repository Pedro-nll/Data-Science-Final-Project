from fastapi import FastAPI
from routes.actors import router as actors_router
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
    title="Hollywood Actors API",
    version="1.0.0"
)

app.include_router(actors_router)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)