"""
Main workflow for the FastAPI application
"""

import uvicorn
from fastapi import FastAPI
from db.database import SessionLocal

from app.api import index, uploadGPX

app = FastAPI()


# Dependency to get DB session
def get_db():
    """
    Get database session
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# Define a root `/` endpoint
app.include_router(index.router)


# Define a POST `/uploadGPX` endpoint
app.include_router(uploadGPX.router)


if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8888, reload=True)
