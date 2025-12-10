Swagger UI → http://127.0.0.1:8000/docs

ReDoc → http://127.0.0.1:8000/redoc

uvicorn main:app --reload

uvicorn main:app --reload --log-level debug

npm run dev

http://localhost:5173

# Wanted functionalities

1. List of all available actors and actresses 
2. About the actor/actresses 
3. All time movie names and years 
4. Awards to actor/actresses in different years 
5. Movie genre of actor/actresses 
6. Average rating of their movies (overall and each year) 
7. Top 5 movies, their respective years and genre

# API Secrets

API Key:

```txt
0a8607c8a14a2432b03163964beb93e1
```

Token de leitura da API:

```txt
eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiIwYTg2MDdjOGExNGEyNDMyYjAzMTYzOTY0YmViOTNlMSIsIm5iZiI6MTc2NTI3ODMxOS43NCwic3ViIjoiNjkzODAyNmYzOTY2MTg1MjBiYWYwMDBhIiwic2NvcGVzIjpbImFwaV9yZWFkIl0sInZlcnNpb24iOjF9.BdwWemHcVWCtePB4AYXw1g2m2CqEYhRIvYr0vfOcqGc
```


# Folder structure

```md
backend/
│
├── main.py
│
├── models/
│   ├── actor_model.py
│   ├── award_model.py
│   ├── movie_model.py
│   └── __init__.py
│
├── scraping/
│   ├── html_parser.py  ---------> Builds the actor names list from the IMDB top 50 list 
│   └── __init__.py
│
├── tmdb/
│   ├── tmdb_client.py ----------> Access the TMDB API and builds the actor objects
│   └── __init__.py
│
└── routes/
    ├── actors.py  --------------> Defines the Fast API routes for actors
    └── __init__.py
```

# Architecture

![Application arch](./Images/Flowchart.png)