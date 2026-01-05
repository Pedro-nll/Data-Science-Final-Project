import { useLocation, useNavigate } from "react-router-dom";
import "../styles/ActorPage.css";

export default function ActorPage() {
  const { state } = useLocation();
  const navigate = useNavigate();

  if (!state?.actor) {
    // Safety fallback (direct URL access)
    navigate("/");
    return null;
  }

  const { actor } = state;

  return (
    <div className="actor-page">
      <button className="back-button" onClick={() => navigate(-1)}>
        ← Back
      </button>

      <div className="actor-header">
        <img src={actor.image_url} alt={actor.name} />
        <div>
          <h1>{actor.name}</h1>
          <p>⭐ {actor.average_rating}</p>
          <p>{actor.genres.join(", ")}</p>
        </div>
      </div>
    </div>
  );
}
