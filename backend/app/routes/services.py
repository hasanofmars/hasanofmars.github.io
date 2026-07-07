from fastapi import APIRouter, Depends, HTTPException
from typing import List
from bson import ObjectId
from app.database import get_db, serialize_doc, serialize_docs
from app.schemas import ServiceCreate, ServiceUpdate, ServiceResponse
from app.auth import get_current_user

router = APIRouter(prefix="/api/services", tags=["services"])


@router.get("/", response_model=List[ServiceResponse])
def get_services():
    db = get_db()
    docs = list(db.services.find().sort("order", 1))
    return serialize_docs(docs)


@router.post("/", response_model=ServiceResponse)
def create_service(service: ServiceCreate, _=Depends(get_current_user)):
    db = get_db()
    result = db.services.insert_one(service.model_dump())
    doc = db.services.find_one({"_id": result.inserted_id})
    return serialize_doc(doc)


@router.put("/{service_id}", response_model=ServiceResponse)
def update_service(service_id: str, service: ServiceUpdate, _=Depends(get_current_user)):
    db = get_db()
    data = {k: v for k, v in service.model_dump(exclude_unset=True).items() if v is not None}
    if not data:
        raise HTTPException(status_code=400, detail="No fields to update")
    result = db.services.update_one({"_id": ObjectId(service_id)}, {"$set": data})
    if result.matched_count == 0:
        raise HTTPException(status_code=404, detail="Service not found")
    doc = db.services.find_one({"_id": ObjectId(service_id)})
    return serialize_doc(doc)


@router.delete("/{service_id}")
def delete_service(service_id: str, _=Depends(get_current_user)):
    db = get_db()
    result = db.services.delete_one({"_id": ObjectId(service_id)})
    if result.deleted_count == 0:
        raise HTTPException(status_code=404, detail="Service not found")
    return {"message": "Service deleted successfully"}
