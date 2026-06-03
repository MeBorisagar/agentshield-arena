import { AgentCard } from "@/components/agent-card";
import { getAgents } from "@/lib/api";

export default async function AgentsPage() {
  const agents = await getAgents();

  return (
    <main className="container mx-auto p-8">
      <h1 className="text-3xl font-bold mb-6">
        Registered Agents
      </h1>

      <div className="grid gap-4">
        {agents.map((agent) => (
          <AgentCard
            key={agent.id}
            agent={agent}
          />
        ))}
      </div>
    </main>
  );
}