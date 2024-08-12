"""
API POST route for uploading GPX file
"""

import os
import shutil
from fastapi import APIRouter, File, Form, UploadFile

router = APIRouter()

# TODO move to env
UPLOAD_FOLDER = "uploads"
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)


@router.post("uploadGPX")
async def upload_file(
    file: UploadFile = File(...),
    valid_until: str = Form(None),
    # TODO db: add database session here
) -> None:
    """
    POST upload gpx route
    """
    # TODO: file verification
    file_path = os.path.join(UPLOAD_FOLDER, file.filename)
    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    return valid_until
