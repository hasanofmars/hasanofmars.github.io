import os
import shutil
from fastapi import APIRouter, UploadFile, File, HTTPException
from app.auth import get_current_user
from fastapi import Depends

router = APIRouter(prefix="/api/upload", tags=["upload"])

# Path to frontend public images directory (relative to project root)
BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))), ".."))
FRONTEND_IMG_DIR = os.path.join(BASE_DIR, "frontend", "public", "images")
os.makedirs(FRONTEND_IMG_DIR, exist_ok=True)


@router.post("/avatar")
async def upload_avatar(file: UploadFile = File(...), _=Depends(get_current_user)):
    # Validate file type
    if not file.content_type or not file.content_type.startswith("image/"):
        raise HTTPException(status_code=400, detail="Only image files are allowed")

    # Save to public/images/profile.jpg
    file_path = os.path.join(FRONTEND_IMG_DIR, "profile.jpg")

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    return {"message": "Avatar uploaded successfully", "path": "/images/profile.jpg"}
