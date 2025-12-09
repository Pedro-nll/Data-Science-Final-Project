import requests
from typing import List, Optional
from models.actor_model import Actor
from models.movie_model import Movie
from scraping.html_parser import get_actor_names

API_KEY = "0a8607c8a14a2432b03163964beb93e1"
BASE_URL = "https://api.themoviedb.org/3"

TMDB_IMAGE_BASE = "https://image.tmdb.org/t/p/w500"

# Uses the actor name gotten from the IMDB list to get the actor info
# returns a object with id in the TMDB API, name, URL to actor's profile image and other attributes
def search_actor(name: str) -> Optional[dict]:
    url = f"{BASE_URL}/search/person"
    params = {"api_key": API_KEY, "query": name}

    response = requests.get(url, params=params)
    response.raise_for_status()

    results = response.json().get("results", [])
    return results[0] if results else None

# Returns a object with more in depth details about the actors, I need this to get the actor bio
def get_actor_details(actor_id):
    url = f"{BASE_URL}/person/{actor_id}"
    params = {"api_key": API_KEY}
    response = requests.get(url, params=params)
    return response.json()

# Returns a JSON object with genres ids and names
# I need this as a dict to match the genre ID returned in the movies API to the proper genre name
def get_movie_genre_list():
    url = f"{BASE_URL}/genre/movie/list"
    params = {"api_key": API_KEY}
    response = requests.get(url, params=params)
    return response.json()

def get_actor_movie_credits(actor_id: str):
    url = f"{BASE_URL}/person/{actor_id}/movie_credits"
    params = {"api_key": API_KEY}
    response = requests.get(url, params=params)
    response.raise_for_status()
    return response.json()

def build_movie_list(movie_credits: dict, genre_lookup: dict):
    movies = []

    for item in movie_credits.get("cast", []):
        title = item.get("title") or item.get("original_title")
        rating = item.get("vote_average")
        cover_path = item.get("backdrop_path")
        cover_img_url = TMDB_IMAGE_BASE + cover_path if cover_path else None
        release_date = item.get("release_date") or ""
        year = int(release_date[:4]) if release_date else None

        # Convert genre IDs into names
        genres = [genre_lookup.get(gid, "Unknown") for gid in item.get("genre_ids", [])]
        
        if "Documentary" in genres:
            continue

        movie = Movie(
            title=title,
            year=year,
            rating=rating,
            genres=genres,
            cover_url=cover_img_url
        )
        movies.append(movie)

    # Sort by rating descending
    movies.sort(key=lambda m: (m.rating or 0), reverse=True)

    return movies

def build_actor_from_tmdb(name: str) -> Optional[Actor]:
    """
    Searches TMDB using actor name and constructs a full Actor object
    including biography, filmography, genres, and average rating.
    """
    data = search_actor(name)
    if not data:
        print(f"[WARN] No TMDB result found for: {name}")
        return None

    actor_id = data["id"]
    profile_path = data.get("profile_path")
    image_url = TMDB_IMAGE_BASE + profile_path if profile_path else None

    # --- Actor details (bio) ---
    actor_details = get_actor_details(actor_id)
    bio = actor_details.get("biography")

    # --- Genre Lookup Table ---
    genre_list = get_movie_genre_list().get("genres", [])
    genre_lookup = {g["id"]: g["name"] for g in genre_list}

    # --- Movie credits ---
    movie_credits = get_actor_movie_credits(actor_id)
    movie_list = build_movie_list(movie_credits, genre_lookup)

    # --- Compute avg rating ---
    ratings = [m.rating for m in movie_list if m.rating]
    avg_rating = round(sum(ratings) / len(ratings), 2) if ratings else None

    # --- Compute actor's overall genre list ---
    all_genres = {genre for m in movie_list for genre in m.genres}
    genres = sorted(list(all_genres))

    actor = Actor(
        id=str(actor_id),
        name=name,
        image_url=image_url,
        average_rating=avg_rating,
        genres=genres,
        bio=bio,
        movies=movie_list,
        awards=[] 
    )

    return actor



def get_all_actors() -> List[Actor]:
    """
    Uses the IMDb scraper to get the list of actor names,
    then fetches TMDB info for each.
    """
    names = get_actor_names()
    actors = []

    for name in names:
        actor = build_actor_from_tmdb(name)
        if actor:
            actors.append(actor)

    return actors