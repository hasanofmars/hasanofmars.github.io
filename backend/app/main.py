from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from app.routes import projects, skills, profile, auth as auth_routes, upload, homepage as homepage_routes, services as services_routes
from app.database import get_db
from app.models import DEFAULT_PROFILE, DEFAULT_HOMEPAGE, DEFAULT_SERVICES

app = FastAPI(
    title="Portfolio API",
    description="Portfolio backend for M Hasan",
    version="2.0.0",
)


@app.on_event("startup")
def startup():
    """Auto-seed database on first run."""
    try:
        db = get_db()
        # Test connection
        db.command("ping")
        print("✅ MongoDB connected successfully")

        if db.profile.count_documents({}) == 0:
            db.profile.insert_one(dict(DEFAULT_PROFILE))
            db.homepage.insert_one(dict(DEFAULT_HOMEPAGE))
            db.services.insert_many(DEFAULT_SERVICES)
            skills_data = [
                {"name": "Python", "level": 95, "category": "Backend"},
                {"name": "JavaScript / TypeScript", "level": 90, "category": "Frontend"},
                {"name": "React / Astro", "level": 88, "category": "Frontend"},
                {"name": "FastAPI / Django", "level": 92, "category": "Backend"},
                {"name": "Penetration Testing", "level": 90, "category": "Security"},
                {"name": "Network Security", "level": 88, "category": "Security"},
                {"name": "Web Security (OWASP)", "level": 92, "category": "Security"},
                {"name": "Docker / Kubernetes", "level": 85, "category": "DevOps"},
                {"name": "MongoDB / PostgreSQL", "level": 87, "category": "Database"},
                {"name": "Cloud (AWS / Azure)", "level": 82, "category": "DevOps"},
            ]
            db.skills.insert_many(skills_data)
            print("✅ Database auto-seeded with default data")
    except Exception as e:
        print(f"❌ MongoDB connection failed: {e}")
        print("   Make sure MONGO_URI env variable is set correctly in Render dashboard")
        print("   Format: mongodb+srv://<user>:<password>@<cluster>.mongodb.net/portfolio_db?retryWrites=true&w=majority")

# CORS configuration — allow all origins for deployment
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Register routers
app.include_router(projects.router)
app.include_router(skills.router)
app.include_router(profile.router)
app.include_router(auth_routes.router)
app.include_router(upload.router)
app.include_router(homepage_routes.router)
app.include_router(services_routes.router)

# Serve uploaded files (avatars)
import os
uploads_dir = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "uploads")
os.makedirs(uploads_dir, exist_ok=True)
app.mount("/uploads", StaticFiles(directory=uploads_dir), name="uploads")


@app.get("/api/health")
def health_check():
    try:
        db = get_db()
        db.command("ping")
        return {"status": "ok", "message": "Portfolio API is running", "db": "MongoDB connected"}
    except Exception as e:
        return {"status": "error", "message": f"MongoDB: {str(e)[:100]}", "db": "disconnected"}
