import { useActorsContext } from "../context/ActorsContext";
import ActorCard from "../components/ActorCard";
import "../styles/LandingPage.css";

export default function LandingPage() {
  const { actors, loading, error } = useActorsContext();

  if (loading) return <div className="loading">Loading actors…</div>;
  if (error) return <div className="error">{error}</div>;

  return (
    <div className="landing-container">
      <h1 className="landing-title">THE GOATS</h1>

      <div className="actors-scroll-container">
        {actors.map(actor => (
          <ActorCard key={actor.id} actor={actor} />
        ))}
      </div>
    </div>
  );
}
