from pymongo import MongoClient
from pymongo.server_api import ServerApi
import os
from dotenv import load_dotenv

load_dotenv()

MONGO_URI = os.getenv("MONGO_URI", "mongodb://localhost:27017")
MONGO_DB = os.getenv("MONGO_DB", "portfolio_db")

client = MongoClient(MONGO_URI, server_api=ServerApi('1'))
db = client[MONGO_DB]


def get_db():
    return db


# Helper to convert ObjectId to string
def serialize_doc(doc):
    if doc and "_id" in doc:
        doc["_id"] = str(doc["_id"])
        doc["id"] = doc["_id"]
    return doc


def serialize_docs(docs):
    return [serialize_doc(doc) for doc in docs]
