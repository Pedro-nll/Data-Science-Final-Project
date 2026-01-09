# Hollywood Actors & Actresses Data Explorer

## Academic Information

**Course:** Applied Data Science with Python  
**Semester:** WiSe 25/26  

**Instructor:**  
Mr. Lengyel – IN, IT  

**Submission Date:**  
December 12, 2025  

**Student:**  
Pedro Negri Leão Lambert  

**Program:**  
IN / IT – OTH Regensburg  

---

## Project Overview

The primary objective of this project is to apply key data science methodologies, to create a user-friendly software application.

The project involves extracting information about the **top 50 popular Hollywood actors and actresses** from a IMDb list, processing this data, and presenting it in a new, interactive format. Rather than dealing with purely unstructured data, the challenge lies in mining **semi-structured HTML content** from the web and transforming it into a clean, actionable dataset that can be easily explored by users through a modern web interface.

This project serves as a practical application of the **full data pipeline**, from extraction and cleaning to aggregation and final presentation using a **FastAPI backend** and a **React frontend**.

---


## Tech Stack

### Backend
- Python
- FastAPI
- Uvicorn
- Requests / BeautifulSoup (HTML scraping)
- TMDB API

### Frontend
- React
- Vite
- JavaScript / TypeScript
- npm

---

## How to Run the Project

### 1. Clone the Repository

```bash
git clone https://github.com/Pedro-nll/Data-Science-Final-Project.git
cd Data-Science-Final-Project
```

### 2. Setup backend

```bash
pip install -r requirements.txt
cd backend
uvicorn main:app --reload
```

The backend will be available at:

- API base: http://127.0.0.1:8000
- Swagger UI: http://127.0.0.1:8000/docs
- ReDoc: http://127.0.0.1:8000/redoc

### 3. Setup frontend

Open a new terminal on the root of the project.

```bash
cd frontend
npm install
npm run dev
```

The frontend will be available at: http://localhost:5173

### 4. Application Usage

Once both backend and frontend are running:

The frontend React application communicates with the FastAPI backend.

The backend scrapes IMDb data, enriches it with TMDB API data, and exposes it through REST endpoints.

The frontend displays actor information, movie statistics, ratings, and awards in an interactive interface.

# Implemented / Target Functionalities

1. List of all available actors and actresses
2. Detailed actor/actress profiles
3. Complete movie list with release years
4. Awards received by actors/actresses by year
5. Movie genres associated with actors/actresses
6. Average movie ratings (overall and per year)
7. Top 5 movies with year and genre

# API Secrets (Academic Use Only)

These tokens are intentionally exposed for academic purposes only.

TMDB API Key
0a8607c8a14a2432b03163964beb93e1

TMDB Read Access Token
eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiIwYTg2MDdjOGExNGEyNDMyYjAzMTYzOTY0YmViOTNlMSIsIm5iZiI6MTc2NTI3ODMxOS43NCwic3ViIjoiNjkzODAyNmYzOTY2MTg1MjBiYWYwMDBhIiwic2NvcGVzIjpbImFwaV9yZWFkIl0sInZlcnNpb24iOjF9.BdwWemHcVWCtePB4AYXw1g2m2CqEYhRIvYr0vfOcqGc

# Backend folder structure

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
│   ├── html_parser.py   # Builds actor name list from IMDb Top 50
│   └── __init__.py
│
├── tmdb/
│   ├── tmdb_client.py   # TMDB API integration and actor data builder
│   └── __init__.py
│
└── routes/
    ├── actors.py        # FastAPI routes related to actors
    └── __init__.py
```

# Architecture 

![Application arch](./Images/Flowchart.png)