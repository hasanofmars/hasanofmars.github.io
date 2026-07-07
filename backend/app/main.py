from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routes import projects, skills, profile, auth as auth_routes, upload, homepage as homepage_routes, services as services_routes

app = FastAPI(
    title="Portfolio API",
    description="Portfolio backend for M Hasan",
    version="2.0.0",
)

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


@app.get("/api/health")
def health_check():
    return {"status": "ok", "message": "Portfolio API is running", "db": "MongoDB"}
