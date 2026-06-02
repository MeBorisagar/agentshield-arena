from fastapi import APIRouter
from fastapi import Depends

from sqlalchemy.orm import Session

from app.db.session import get_db
from app.schemas.agent import AgentCreate
from app.schemas.agent import AgentResponse
from app.services.agent_service import AgentService

router = APIRouter(
    prefix="/agents",
    tags=["agents"],
)


@router.post(
    "",
    response_model=AgentResponse,
)
def create_agent(
    agent: AgentCreate,
    db: Session = Depends(get_db),
):

    return AgentService.create(
        db=db,
        agent_data=agent,
    )