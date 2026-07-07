"""Seed the MongoDB database with initial portfolio data."""
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from app.database import get_db

db = get_db()

# Clear existing data
db.projects.delete_many({})
db.skills.delete_many({})
db.services.delete_many({})
db.profile.delete_many({})
db.homepage.delete_many({})

print("Cleared existing data.")

# Seed profile
profile = {
    "name": "M Hasan",
    "title": "Full Stack Developer & Cybersecurity Expert",
    "location": "Dhaka, Bangladesh",
    "bio": "I'm M Hasan, a passionate Full Stack Developer and Cybersecurity Expert based in Dhaka, Bangladesh. With over 5 years of experience, I specialize in building secure, scalable web applications and protecting digital infrastructure from emerging threats.",
    "avatar_url": "/images/profile.jpg",
    "email": "mhasan@security.dev",
    "github": "https://github.com/mhasan",
    "linkedin": "https://linkedin.com/in/mhasan",
    "twitter": "https://twitter.com/mhasan",
    "website": "",
}
db.profile.insert_one(profile)
print("✅ Profile seeded.")

# Seed homepage
homepage = {
    "hero_badge": "Cybersecurity Expert & Developer",
    "hero_title": "Hi, I'm M Hasan",
    "hero_typing": "I build secure & scalable web solutions",
    "hero_description": "Full Stack Developer & Cybersecurity Expert based in Dhaka, Bangladesh. Passionate about building secure, high-performance web applications and protecting digital infrastructure.",
    "hero_status": "Available for projects",
    "stats": [
        {"number": "5+", "label": "Years Experience"},
        {"number": "50+", "label": "Projects Done"},
        {"number": "100+", "label": "Happy Clients"},
    ],
    "featured_title": "Featured Projects",
    "featured_subtitle": "Highlighting my most impactful work in cybersecurity and web development",
    "services_title": "What I Do",
    "services_subtitle": "Comprehensive cybersecurity and development services",
}
db.homepage.insert_one(homepage)
print("✅ Homepage seeded.")

# Seed services
services = [
    {"title": "Web Development", "description": "Modern, responsive web applications with React, Astro, FastAPI, and secure backend systems.", "icon": "code", "order": 1},
    {"title": "Penetration Testing", "description": "Comprehensive security assessments, vulnerability scanning, and ethical hacking services.", "icon": "shield", "order": 2},
    {"title": "Security Consulting", "description": "Architecture review, security best practices, compliance audits, and threat modeling.", "icon": "tool", "order": 3},
    {"title": "Cloud Security", "description": "Secure cloud architecture design, implementation, and monitoring on AWS, Azure, and GCP.", "icon": "cloud", "order": 4},
]
db.services.insert_many(services)
print("✅ Services seeded.")

# Seed skills
skills = [
    {"name": "Python", "level": 95, "category": "Backend"},
    {"name": "JavaScript / TypeScript", "level": 90, "category": "Frontend"},
    {"name": "React / Astro", "level": 88, "category": "Frontend"},
    {"name": "FastAPI / Django", "level": 92, "category": "Backend"},
    {"name": "Node.js", "level": 85, "category": "Backend"},
    {"name": "Penetration Testing", "level": 90, "category": "Security"},
    {"name": "Network Security", "level": 88, "category": "Security"},
    {"name": "Web Security (OWASP)", "level": 92, "category": "Security"},
    {"name": "Docker / Kubernetes", "level": 85, "category": "DevOps"},
    {"name": "MongoDB / PostgreSQL", "level": 87, "category": "Database"},
    {"name": "Cloud (AWS / Azure)", "level": 82, "category": "DevOps"},
    {"name": "Cryptography", "level": 80, "category": "Security"},
]
db.skills.insert_many(skills)
print("✅ Skills seeded.")

# Seed projects
projects = [
    {"title": "NetShield Pro", "description": "Enterprise-grade network security scanner with real-time threat detection and automated incident response system.", "tech_stack": "Python,Scapy,MongoDB,Docker", "live_url": "#", "github_url": "#", "category": "Cybersecurity", "featured": True, "created_at": "2026-06-15T10:00:00Z"},
    {"title": "SecureVault Cloud", "description": "End-to-end encrypted cloud storage with zero-knowledge architecture, file integrity monitoring, and secure sharing.", "tech_stack": "React,Node.js,AES-256,PostgreSQL", "live_url": "#", "github_url": "#", "category": "Security", "featured": True, "created_at": "2026-05-20T10:00:00Z"},
    {"title": "WebDefender WAF", "description": "AI-powered web application firewall with DDoS mitigation, bot detection, and real-time traffic analysis.", "tech_stack": "FastAPI,Redis,TensorFlow,Nginx", "live_url": "#", "github_url": "#", "category": "Cybersecurity", "featured": True, "created_at": "2026-04-10T10:00:00Z"},
    {"title": "BugTracker Pro", "description": "Advanced bug tracking and project management platform with sprint planning and team collaboration tools.", "tech_stack": "React,Django,PostgreSQL,Docker", "live_url": "#", "github_url": "#", "category": "Web App", "featured": False, "created_at": "2026-03-05T10:00:00Z"},
    {"title": "PortScan Analyzer", "description": "High-performance port scanning and service discovery tool with detailed reporting and vulnerability correlation.", "tech_stack": "Python,Asyncio,PostgreSQL,Redis", "live_url": "#", "github_url": "#", "category": "Security Tool", "featured": False, "created_at": "2026-02-01T10:00:00Z"},
    {"title": "E-Commerce Platform", "description": "Full-featured e-commerce platform with payment gateway integration, inventory management, and analytics dashboard.", "tech_stack": "Next.js,FastAPI,MongoDB,Stripe", "live_url": "#", "github_url": "#", "category": "Web App", "featured": False, "created_at": "2026-01-15T10:00:00Z"},
    {"title": "LogWatch SIEM", "description": "Security information and event management system with real-time log analysis, alerting, and compliance reporting.", "tech_stack": "Python,Elasticsearch,Kibana,Docker", "live_url": "#", "github_url": "#", "category": "Security", "featured": False, "created_at": "2025-12-01T10:00:00Z"},
    {"title": "DevOps Pipeline", "description": "Automated CI/CD pipeline with security scanning, container orchestration, and infrastructure as code.", "tech_stack": "GitHub Actions,Docker,K8s,Terraform", "live_url": "#", "github_url": "#", "category": "DevOps", "featured": False, "created_at": "2025-11-10T10:00:00Z"},
]
db.projects.insert_many(projects)
print("✅ Projects seeded.")

print("\n🎉 Database seeded successfully!")
print(f"   Collections: {db.list_collection_names()}")
