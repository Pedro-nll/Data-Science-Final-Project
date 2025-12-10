import { useEffect, useState } from "react";
import { fetchActors } from "../api/actors";

export default function LandingPage() {
  const [actors, setActors] = useState([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    async function loadActors() {
      try {
        const data = await fetchActors();
        setActors(data);
      } catch (err) {
        console.error("Failed to load actors:", err);
      } finally {
        setLoading(false);
      }
    }

    loadActors();
  }, []);

  if (loading) return <p>Loading actors...</p>;

  return (
    <div>
      <h1>Popular Actors</h1>
      <ul>
        {actors.map(actor => (
          <li key={actor.id}>{actor.name}</li>
        ))}
      </ul>
    </div>
  );
}
