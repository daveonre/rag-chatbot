from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.database import db
from app.api.documents import router as documents_router
from app.api.chat import router as chat_router


app = FastAPI(
    title="Dawit's RAG Chatbot API",
    version="1.0.0"
)

# 1. DEFINE ORIGINS FIRST
origins = [
    "http://localhost:3000",
    "http://localhost:5173",
    "http://127.0.0.1:5173",
    "http://127.0.0.1:3000",
    "http://localhost"
]

# 2. PASS IT TO THE MIDDLEWARE AFTER IT IS DEFINED
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(documents_router)
app.include_router(chat_router)


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
