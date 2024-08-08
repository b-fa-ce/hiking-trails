from fastapi import FastAPI, File, UploadFile, Form
import os
from db.database import SessionLocal
import shutil
import uvicorn

app = FastAPI()

# TODO move to env
UPLOAD_FOLDER = 'uploads'
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

# Dependency to get DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Define a root `/` endpoint
@app.get('/')
async def index():
    return {'ok': True}

# Define a POST `/uploadGPX` endpoint
@app.post('uploadGPX')
async def upload_file(
    file: UploadFile = File(...),
    valid_until: str = Form(None),
    # TODO db: add database session here
) -> None:
    # TODO: file verification
    file_path = os.path.join(UPLOAD_FOLDER, file.filename)
    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)


    return None


if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8888, reload= True)
