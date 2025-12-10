import React from "react";
import "./../styles/ActorCard.css";

export default function ActorCard({ actor }) {
  return (
    <div className="actor-card">
      <img
        src={actor.image_url}
        alt={actor.name}
        className="actor-image"
      />

      <div className="actor-info">
        <h3 className="actor-name">{actor.name}</h3>

        {actor.average_rating && (
          <p className="actor-rating">
            ⭐ {actor.average_rating}
          </p>
        )}

        {actor.genres && actor.genres.length > 0 && (
          <p className="actor-genres">
            {actor.genres.slice(0, 3).join(", ")}
          </p>
        )}
      </div>
    </div>
  );
}
