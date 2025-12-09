from typing import List, Optional
from pydantic import BaseModel

from models.award_model import Award
from models.movie_model import Movie

class Actor(BaseModel):
    id: str                                 # according to the TMDB API
    name: str                               
    image_url: Optional[str] = None         # actor profile photo
    average_rating: Optional[float] = None  # average movie rating
    genres: List[str] = []                  # according to the TMDB API
    bio: Optional[str] = None               # "about" section
    movies: List[Movie] = []                # sorted by rating descending
    awards: List[Award] = []                
