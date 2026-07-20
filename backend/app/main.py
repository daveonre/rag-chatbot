from fastapi import FastAPI
from app.database import db
from app.api.documents import router as documents_router


app = FastAPI(
    title="Dawit's RAG Chatbot API",
    version="1.0.0"
)

app.include_router(documents_router)


@app.get("/")
async def root():
    return {
        "message": "Hello , Your RAG Chatbot API is running"
    }


@app.get("/health")
async def health_check():
    try:
        # Basic connectivity check
        await db.command("ping")

        # Get MongoDB version + build details
        build_info = await db.command("buildInfo")

        return {
            "status": "healthy",
            "database": "MongoDB connected successfully",
            "mongodb_version": build_info.get("version"),
            "git_version": build_info.get("gitVersion"),
            "modules": build_info.get("modules", [])
        }

    except Exception as e:
        return {
            "status": "unhealthy",
            "error": str(e)
        }
