import React from "react";
import { useActors } from "../hooks/useActors";
import ActorCard from "../components/ActorCard";
import "../styles/LandingPage.css";

export default function LandingPage() {
  const { actors, loading, error } = useActors();

  if (loading) return <div className="loading">Loading actors…<br/>it does takes a while, about a minute or so...<br/>sorry :(</div>;
  if (error) return <div className="error">{error}</div>;

  return (
    <div className="landing-container">
      <h1 className="landing-title">Popular Actors & Actresses</h1>

      <div className="actors-scroll-container">
        {actors.map((actor) => (
          <ActorCard key={actor.id} actor={actor} />
        ))}
      </div>
    </div>
  );
}
