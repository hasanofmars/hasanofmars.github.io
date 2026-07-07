from pydantic import BaseModel
from typing import Optional, List
from datetime import datetime


# ---- Project Schemas ----
class ProjectBase(BaseModel):
    title: str
    description: Optional[str] = None
    image_url: Optional[str] = None
    tech_stack: Optional[str] = None
    live_url: Optional[str] = None
    github_url: Optional[str] = None
    category: Optional[str] = None
    featured: bool = False


class ProjectCreate(ProjectBase):
    pass


class ProjectUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    image_url: Optional[str] = None
    tech_stack: Optional[str] = None
    live_url: Optional[str] = None
    github_url: Optional[str] = None
    category: Optional[str] = None
    featured: Optional[bool] = None


class ProjectResponse(ProjectBase):
    id: str
    created_at: Optional[str] = None


# ---- Skill Schemas ----
class SkillBase(BaseModel):
    name: str
    level: int = 50
    category: Optional[str] = None
    icon: Optional[str] = None


class SkillCreate(SkillBase):
    pass


class SkillUpdate(BaseModel):
    name: Optional[str] = None
    level: Optional[int] = None
    category: Optional[str] = None
    icon: Optional[str] = None


class SkillResponse(SkillBase):
    id: str


# ---- Profile Schemas ----
class ProfileBase(BaseModel):
    name: str = "M Hasan"
    title: str = "Full Stack Developer & Cybersecurity Expert"
    location: str = "Dhaka, Bangladesh"
    bio: Optional[str] = None
    avatar_url: Optional[str] = None
    email: Optional[str] = None
    github: Optional[str] = None
    linkedin: Optional[str] = None
    twitter: Optional[str] = None
    website: Optional[str] = None


class ProfileUpdate(ProfileBase):
    pass


class ProfileResponse(ProfileBase):
    id: Optional[str] = None


# ---- Homepage Schemas ----
class StatItem(BaseModel):
    number: str = "5+"
    label: str = "Years Experience"


class HomepageUpdate(BaseModel):
    hero_badge: Optional[str] = None
    hero_title: Optional[str] = None
    hero_typing: Optional[str] = None
    hero_description: Optional[str] = None
    hero_status: Optional[str] = None
    stats: Optional[List[StatItem]] = None
    featured_title: Optional[str] = None
    featured_subtitle: Optional[str] = None
    services_title: Optional[str] = None
    services_subtitle: Optional[str] = None


class HomepageResponse(BaseModel):
    id: Optional[str] = None
    hero_badge: str = ""
    hero_title: str = ""
    hero_typing: str = ""
    hero_description: str = ""
    hero_status: str = ""
    stats: List[StatItem] = []
    featured_title: str = ""
    featured_subtitle: str = ""
    services_title: str = ""
    services_subtitle: str = ""


# ---- Service Schemas ----
class ServiceBase(BaseModel):
    title: str
    description: str
    icon: str = "code"
    order: int = 0


class ServiceCreate(ServiceBase):
    pass


class ServiceUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    icon: Optional[str] = None
    order: Optional[int] = None


class ServiceResponse(ServiceBase):
    id: str


# ---- Auth Schemas ----
class Token(BaseModel):
    access_token: str
    token_type: str


class LoginRequest(BaseModel):
    username: str
    password: str


# ---- Dashboard Stats ----
class DashboardStats(BaseModel):
    total_projects: int = 0
    total_skills: int = 0
    featured_projects: int = 0
    total_services: int = 0
    security_tools: int
