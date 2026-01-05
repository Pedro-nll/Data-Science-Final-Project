import { useLocation, useNavigate } from "react-router-dom";
import React, { useState } from "react";
import "../styles/ActorPage.css";

export default function ActorPage() {
  const { state } = useLocation();
  const navigate = useNavigate();
  const [expanded, setExpanded] = useState(false);

  if (!state?.actor) {
    navigate("/");
    return null;
  }

  const { actor } = state;

  return (
    <div className="actor-page">
      <button className="back-button" onClick={() => navigate(-1)}>
        ← Back
      </button>

      {/* HEADER */}
      <section className="actor-header">
        <img
          src={actor.image_url}
          alt={actor.name}
          className="actor-portrait"
        />

        <div className="actor-header-info">
          <h1>{actor.name}</h1>
          <p className="actor-rating">⭐ {actor.average_rating}</p>
          <p className="actor-genres">
            {actor.genres.join(" • ")}
          </p>
        </div>
      </section>

      {/* BIO */}
      <section className="actor-bio">
        <h2>About the actor</h2>

        <div className={`bio-text ${expanded ? "expanded" : ""}`}>
          {actor.bio}
        </div>

        <button
          className="bio-toggle"
          onClick={() => setExpanded(prev => !prev)}
        >
          {expanded ? "Show less" : "Read more"}
        </button>
      </section>

      {/* MOVIES */}
      <section className="actor-movies">
        <h2>Movies</h2>

        <div className="movies-grid">
          {actor.movies.map((movie, idx) => (
            <div key={idx} className="movie-card">
              <img
                src={movie.cover_url}
                alt={movie.title}
              />

              <div className="movie-info">
                <h3>{movie.title}</h3>
                <p>{movie.year}</p>
                <p>⭐ {movie.rating.toFixed(1)}</p>
                <p className="movie-genres">
                  {movie.genres.join(", ")}
                </p>
              </div>
            </div>
          ))}
        </div>
      </section>

      {/* AWARDS */}
      <section className="actor-awards">
        <h2>Awards</h2>

        {actor.awards.length === 0 ? (
          <p className="empty-state">
            No awards information available.
          </p>
        ) : (
          <ul>
            {actor.awards.map((award, idx) => (
              <li key={idx}>{award}</li>
            ))}
          </ul>
        )}
      </section>
    </div>
  );
}
