import os
import shutil
from fastapi import APIRouter, UploadFile, File, HTTPException
from fastapi.staticfiles import StaticFiles
from app.auth import get_current_user
from fastapi import Depends

router = APIRouter(prefix="/api/upload", tags=["upload"])

# Save avatars to local uploads directory (works on Render)
UPLOAD_DIR = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))), "uploads")
AVATAR_DIR = os.path.join(UPLOAD_DIR, "avatars")
os.makedirs(AVATAR_DIR, exist_ok=True)


def mount_static(app):
    """Call this from main.py to serve uploaded files."""
    if os.path.exists(UPLOAD_DIR):
        app.mount("/uploads", StaticFiles(directory=UPLOAD_DIR), name="uploads")


@router.post("/avatar")
async def upload_avatar(file: UploadFile = File(...), _=Depends(get_current_user)):
    # Validate file type
    if not file.content_type or not file.content_type.startswith("image/"):
        raise HTTPException(status_code=400, detail="Only image files are allowed")

    # Save to uploads/avatars/profile.jpg
    file_path = os.path.join(AVATAR_DIR, "profile.jpg")

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    avatar_url = f"/uploads/avatars/profile.jpg"
    return {"message": "Avatar uploaded successfully", "path": avatar_url}
