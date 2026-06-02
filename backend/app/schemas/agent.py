from datetime import datetime

from pydantic import BaseModel
from app.schemas.enums import AgentType

class AgentCreate(BaseModel):
    name: str
    agent_type: AgentType
    endpoint: str


class AgentResponse(BaseModel):
    id: int
    name: str
    agent_type: str
    endpoint: str
    created_at: datetime

    model_config = {
        "from_attributes": True
    }