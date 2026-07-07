from fastapi import APIRouter, Depends, HTTPException
from typing import List
from bson import ObjectId
from app.database import get_db, serialize_doc, serialize_docs
from app.schemas import SkillCreate, SkillUpdate, SkillResponse
from app.auth import get_current_user

router = APIRouter(prefix="/api/skills", tags=["skills"])


@router.get("/", response_model=List[SkillResponse])
def get_skills():
    db = get_db()
    docs = list(db.skills.find())
    return serialize_docs(docs)


@router.post("/", response_model=SkillResponse)
def create_skill(skill: SkillCreate, _=Depends(get_current_user)):
    db = get_db()
    result = db.skills.insert_one(skill.model_dump())
    doc = db.skills.find_one({"_id": result.inserted_id})
    return serialize_doc(doc)


@router.put("/{skill_id}", response_model=SkillResponse)
def update_skill(skill_id: str, skill: SkillUpdate, _=Depends(get_current_user)):
    db = get_db()
    data = {k: v for k, v in skill.model_dump(exclude_unset=True).items() if v is not None}
    if not data:
        raise HTTPException(status_code=400, detail="No fields to update")
    result = db.skills.update_one({"_id": ObjectId(skill_id)}, {"$set": data})
    if result.matched_count == 0:
        raise HTTPException(status_code=404, detail="Skill not found")
    doc = db.skills.find_one({"_id": ObjectId(skill_id)})
    return serialize_doc(doc)


@router.delete("/{skill_id}")
def delete_skill(skill_id: str, _=Depends(get_current_user)):
    db = get_db()
    result = db.skills.delete_one({"_id": ObjectId(skill_id)})
    if result.deleted_count == 0:
        raise HTTPException(status_code=404, detail="Skill not found")
    return {"message": "Skill deleted successfully"}
