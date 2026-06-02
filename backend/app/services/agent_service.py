from sqlalchemy.orm import Session

from app.models.agent import Agent
from app.schemas.agent import AgentCreate


class AgentService:

    @staticmethod
    def create(
        db: Session,
        agent_data: AgentCreate,
    ) -> Agent:

        agent = Agent(
            name=agent_data.name,
            agent_type=agent_data.agent_type,
            endpoint=agent_data.endpoint,
        )

        db.add(agent)

        db.commit()

        db.refresh(agent)

        return agent