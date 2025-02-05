from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import os
from dotenv import load_dotenv
from app.database.database import engine
from app.models import models
from app.routes import auth
from app.routes import exgen
from app.routes import lessons
from app.routes import exercises
from app.routes import progress

# Load environment variables
load_dotenv()

# Create the database tables
models.Base.metadata.create_all(bind=engine)

# Create FastAPI app
app = FastAPI(title="Math Learning API")
app.include_router(auth.router)
app.include_router(exgen.router)
app.include_router(lessons.router)
app.include_router(exercises.router)
app.include_router(progress.router)


# Configure CORS
origins = os.getenv("BACKEND_CORS_ORIGINS", "http://localhost:3000").split(",")
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Root endpoint for testing
@app.get("/")
def read_root():
    return {"status": "healthy"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
