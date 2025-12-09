import requests
from bs4 import BeautifulSoup
import json

# URL of the provided list with top 50 actors
IMDB_URL = "https://www.imdb.com/list/ls053501318/"

def get_actor_names():
    # make a request for the page's content
    response = requests.get(IMDB_URL, headers={"User-Agent": "Mozilla/5.0"})
    response.raise_for_status()

    # Parse the page's content as HTML
    soup = BeautifulSoup(response.text, "html.parser")

    # Find the JSON-LD block containing the list of actors names
    json_ld_tag = soup.find("script", type="application/ld+json")
    if json_ld_tag is None:
        raise ValueError("Could not locate JSON-LD data in the page!")

    data = json.loads(json_ld_tag.string)

    # Extract actor names
    actors = [entry["item"]["name"] for entry in data["itemListElement"]]

    return actors