import os
import shutil
from fastapi import APIRouter, UploadFile, File

router = APIRouter(tags=["files"])

@router.post("/upload-image")
def upload_image(file: UploadFile = File(...)):
    os.makedirs("static/images", exist_ok=True)

    file_path = f"static/images/{file.filename}"

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    return {"image_url": f"/static/images/{file.filename}"}