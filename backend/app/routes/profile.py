from fastapi import APIRouter, Depends, HTTPException
from app.database import get_db, serialize_doc
from app.models import DEFAULT_PROFILE
from app.schemas import ProfileResponse, ProfileUpdate, DashboardStats
from app.auth import get_current_user

router = APIRouter(prefix="/api/profile", tags=["profile"])


@router.get("/", response_model=ProfileResponse)
def get_profile():
    db = get_db()
    doc = db.profile.find_one()
    if not doc:
        db.profile.insert_one(dict(DEFAULT_PROFILE))
        doc = db.profile.find_one()
    return serialize_doc(doc)


@router.put("/", response_model=ProfileResponse)
def update_profile(profile_data: ProfileUpdate, _=Depends(get_current_user)):
    db = get_db()
    data = {k: v for k, v in profile_data.model_dump(exclude_unset=True).items() if v is not None}
    if db.profile.count_documents({}) == 0:
        db.profile.insert_one({**DEFAULT_PROFILE, **data})
    else:
        db.profile.update_one({}, {"$set": data})
    doc = db.profile.find_one()
    return serialize_doc(doc)


@router.get("/stats", response_model=DashboardStats)
def get_dashboard_stats():
    db = get_db()
    total_projects = db.projects.count_documents({})
    total_skills = db.skills.count_documents({})
    featured_projects = db.projects.count_documents({"featured": True})
    total_services = db.services.count_documents({})
    return DashboardStats(
        total_projects=total_projects,
        total_skills=total_skills,
        featured_projects=featured_projects,
        total_services=total_services,
    )
