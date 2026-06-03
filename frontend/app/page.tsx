import Link from "next/link";

export default function HomePage() {
  return (
    <main className="p-8">
      <h1 className="text-4xl font-bold">
        AgentShield Arena
      </h1>

      <Link
        href="/agents"
        className="underline"
      >
        View Agents
      </Link>
    </main>
  );
}