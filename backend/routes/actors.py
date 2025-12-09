from fastapi import APIRouter, HTTPException
from typing import List
from tmdb.tmdb_client import get_all_actors
from models.actor_model import Actor

router = APIRouter(prefix="/actors", tags=["Actors"])

@router.get("/", response_model=List[Actor])
def fetch_actors():
    try:
        actors = get_all_actors()

        if not actors:
            raise HTTPException(status_code=404, detail="No actors found")

        return actors

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
