import axios from "axios";

const API_BASE_URL = "http://localhost:8000"; 

export async function fetchActors() {
  try {
    const response = await axios.get(`${API_BASE_URL}/actors`);
    return response.data;
  } catch (error) {
    console.error("Error fetching actors:", error);
    throw error;
  }
}
