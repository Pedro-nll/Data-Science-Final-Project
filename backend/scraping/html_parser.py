import requests
from bs4 import BeautifulSoup
import json

# URL of the provided list with top 50 actors
IMDB_URL = "https://www.imdb.com/list/ls053501318/"

def get_actor_names():
        # make a request for the page's content
    headers = {
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 "
                    "(KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
        "Accept-Language": "en-US,en;q=0.9",
        "Referer": "https://www.google.com/",
        "Connection": "keep-alive",
    }

    response = requests.get(IMDB_URL, headers=headers, timeout=10)

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