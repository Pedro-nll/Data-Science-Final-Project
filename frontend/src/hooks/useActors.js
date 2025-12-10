import { useEffect, useState } from "react";
import axios from "axios";

export function useActors() {
  const [actors, setActors] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    async function fetchActors() {
      try {
        setLoading(true);

        const response = await axios.get(
          "http://localhost:8000/actors/"
        );

        setActors(response.data);
      } catch (err) {
        console.error("Failed to load actors:", err);
        setError("Unable to load actors.");
      } finally {
        setLoading(false);
      }
    }

    fetchActors();
  }, []);

  return { actors, loading, error };
}
