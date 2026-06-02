from fastapi import FastAPI

app = FastAPI(title="AgentShield Arena")


@app.get("/health")
def health():
    return {"status": "healthy"}