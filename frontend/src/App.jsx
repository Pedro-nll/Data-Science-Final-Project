import { BrowserRouter, Routes, Route } from "react-router-dom";
import LandingPage from "./pages/LandingPage";
import ActorPage from "./pages/ActorPage";
import { ActorsProvider } from "./context/ActorsContext";

export default function App() {
  // Wrap the app with ActorsProvider to provide actors data via context (fetch happens once)
  // Setup routing for landing page and actor detail page
  return (
    <ActorsProvider> 
      <BrowserRouter>
        <Routes>
          <Route path="/" element={<LandingPage />} />
          <Route path="/actor/:id" element={<ActorPage />} />
        </Routes>
      </BrowserRouter>
    </ActorsProvider>
  );
}
