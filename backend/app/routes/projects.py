from fastapi import APIRouter, Depends, HTTPException
from typing import List
from bson import ObjectId
from app.database import get_db, serialize_doc, serialize_docs
from app.schemas import ProjectCreate, ProjectUpdate, ProjectResponse
from app.auth import get_current_user
from datetime import datetime

router = APIRouter(prefix="/api/projects", tags=["projects"])


@router.get("/", response_model=List[ProjectResponse])
def get_projects():
    db = get_db()
    docs = list(db.projects.find().sort("created_at", -1))
    return serialize_docs(docs)


@router.get("/featured", response_model=List[ProjectResponse])
def get_featured_projects():
    db = get_db()
    docs = list(db.projects.find({"featured": True}).sort("created_at", -1))
    return serialize_docs(docs)


@router.get("/{project_id}", response_model=ProjectResponse)
def get_project(project_id: str):
    db = get_db()
    doc = db.projects.find_one({"_id": ObjectId(project_id)})
    if not doc:
        raise HTTPException(status_code=404, detail="Project not found")
    return serialize_doc(doc)


@router.post("/", response_model=ProjectResponse)
def create_project(project: ProjectCreate, _=Depends(get_current_user)):
    db = get_db()
    data = project.model_dump()
    data["created_at"] = datetime.utcnow().isoformat()
    result = db.projects.insert_one(data)
    doc = db.projects.find_one({"_id": result.inserted_id})
    return serialize_doc(doc)


@router.put("/{project_id}", response_model=ProjectResponse)
def update_project(project_id: str, project: ProjectUpdate, _=Depends(get_current_user)):
    db = get_db()
    data = {k: v for k, v in project.model_dump(exclude_unset=True).items() if v is not None}
    if not data:
        raise HTTPException(status_code=400, detail="No fields to update")
    result = db.projects.update_one({"_id": ObjectId(project_id)}, {"$set": data})
    if result.matched_count == 0:
        raise HTTPException(status_code=404, detail="Project not found")
    doc = db.projects.find_one({"_id": ObjectId(project_id)})
    return serialize_doc(doc)


@router.delete("/{project_id}")
def delete_project(project_id: str, _=Depends(get_current_user)):
    db = get_db()
    result = db.projects.delete_one({"_id": ObjectId(project_id)})
    if result.deleted_count == 0:
        raise HTTPException(status_code=404, detail="Project not found")
    return {"message": "Project deleted successfully"}
