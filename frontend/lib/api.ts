import { Agent } from "./types";

const API_URL =
  process.env.NEXT_PUBLIC_API_URL ??
  "http://backend:8000";

export async function getAgents(): Promise<Agent[]> {
  const response = await fetch(
    `${API_URL}/agents`,
    {
      cache: "no-store",
    }
  );

  if (!response.ok) {
    throw new Error("Failed to fetch agents");
  }

  return response.json();
}