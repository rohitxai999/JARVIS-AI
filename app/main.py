from fastapi import FastAPI

from app.api.memory_routes import router as memory_router


app = FastAPI(
    title="JARVIS AI",
    version="0.1.0"
)


app.include_router(memory_router)


@app.get("/")
def root():
    return {
        "message": "JARVIS AI is running",
        "module": "Memory Engine"
    }