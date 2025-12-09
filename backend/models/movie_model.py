from typing import List, Optional
from pydantic import BaseModel

class Movie(BaseModel):
    title: str
    year: Optional[int] = None
    rating: Optional[float] = None
    genres: List[str] = []
    cover_url: Optional[str] = None
