import { Agent } from "@/lib/types";

import {
  Card,
  CardContent,
  CardHeader,
  CardTitle,
} from "@/components/ui/card";

interface AgentCardProps {
  agent: Agent;
}

export function AgentCard({
  agent,
}: AgentCardProps) {
  return (
    <Card>
      <CardHeader>
        <CardTitle>
          {agent.name}
        </CardTitle>
      </CardHeader>

      <CardContent>
        <p>
          Type: {agent.agent_type}
        </p>

        <p className="text-sm text-muted-foreground">
          {agent.endpoint}
        </p>
      </CardContent>
    </Card>
  );
}