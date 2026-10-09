from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import os
from dotenv import load_dotenv
from app.routes.api import router as api_router
from app.database.connection import engine, Base
import app.models.models as models

load_dotenv()

# Create tables if they don't exist
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Portfolio API",
    description="Backend API for Kenil Bhadani's Portfolio",
    version="1.0.0"
)

# CORS config
cors_origins = os.getenv("CORS_ORIGINS", "http://localhost:3000,http://127.0.0.1:8000,http://127.0.0.1:5500,http://localhost:5500").split(",")

app.add_middleware(
    CORSMiddleware,
    allow_origins=cors_origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(api_router, prefix="/api")

@app.get("/")
def read_root():
    return {"message": "Welcome to the Portfolio API"}
