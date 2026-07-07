from fastapi import APIRouter, Depends
from app.database import get_db, serialize_doc
from app.models import DEFAULT_HOMEPAGE
from app.schemas import HomepageUpdate, HomepageResponse
from app.auth import get_current_user

router = APIRouter(prefix="/api/homepage", tags=["homepage"])


@router.get("/", response_model=HomepageResponse)
def get_homepage():
    db = get_db()
    doc = db.homepage.find_one()
    if not doc:
        db.homepage.insert_one(dict(DEFAULT_HOMEPAGE))
        doc = db.homepage.find_one()
    return serialize_doc(doc)


@router.put("/", response_model=HomepageResponse)
def update_homepage(data: HomepageUpdate, _=Depends(get_current_user)):
    db = get_db()
    update_data = {k: v for k, v in data.model_dump(exclude_unset=True).items() if v is not None}
    if db.homepage.count_documents({}) == 0:
        db.homepage.insert_one({**DEFAULT_HOMEPAGE, **update_data})
    else:
        db.homepage.update_one({}, {"$set": update_data})
    doc = db.homepage.find_one()
    return serialize_doc(doc)
