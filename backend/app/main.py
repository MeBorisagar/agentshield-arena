from fastapi import FastAPI

from app.api.agents import router as agents_router

app = FastAPI(
    title="AgentShield Arena",
)

app.include_router(agents_router)


@app.get("/health")
def health():
    return {
        "status": "healthy",
    }