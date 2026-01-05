import React, { createContext, useContext } from "react";
import { useActors } from "../hooks/useActors";

const ActorsContext = createContext(null);

export function ActorsProvider({ children }) {
  const actorsState = useActors(); // fetch happens once and doesn't repeat with navigation

  return (
    <ActorsContext.Provider value={actorsState}>
      {children}
    </ActorsContext.Provider>
  );
}

export function useActorsContext() {
  return useContext(ActorsContext);
}
