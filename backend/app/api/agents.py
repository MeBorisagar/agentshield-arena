from fastapi import APIRouter
from fastapi import Depends

from sqlalchemy.orm import Session

from app.db.session import get_db
from app.schemas.agent import AgentCreate
from app.schemas.agent import AgentResponse
from app.services.agent_service import AgentService

from fastapi import HTTPException

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

@router.get(
    "",
    response_model=list[AgentResponse],
)
def get_agents(
    db: Session = Depends(get_db),
):

    return AgentService.get_all(db)


@router.get(
    "/{agent_id}",
    response_model=AgentResponse,
)
def get_agent(
    agent_id: int,
    db: Session = Depends(get_db),
):

    agent = AgentService.get_by_id(
        db=db,
        agent_id=agent_id,
    )

    if not agent:
        raise HTTPException(
            status_code=404,
            detail="Agent not found",
        )

    return agent