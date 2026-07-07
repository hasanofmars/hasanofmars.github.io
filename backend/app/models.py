# MongoDB document structures (reference only — no schema enforcement)
# Collections: projects, skills, profile, services, homepage
# 
# project:  { _id, title, description, image_url, tech_stack, live_url, github_url, category, featured, created_at }
# skill:    { _id, name, level, category, icon }
# profile:  { _id, name, title, location, bio, avatar_url, email, github, linkedin, twitter, website }
# service:  { _id, title, description, icon, order }
# homepage: { _id, hero_title, hero_subtitle, hero_description, badge_text, typing_text,
#             status_text, stats: [{number, label}], section_titles, social_links }

from datetime import datetime

DEFAULT_PROFILE = {
    "name": "M Hasan",
    "title": "Full Stack Developer & Cybersecurity Expert",
    "location": "Dhaka, Bangladesh",
    "bio": "",
    "avatar_url": "/uploads/avatars/profile.jpg",
    "email": "mhasan@security.dev",
    "github": "https://github.com/mhasan",
    "linkedin": "https://linkedin.com/in/mhasan",
    "twitter": "https://twitter.com/mhasan",
    "website": "",
}

DEFAULT_HOMEPAGE = {
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

DEFAULT_SERVICES = [
    {"title": "Web Development", "description": "Modern, responsive web applications with React, Astro, FastAPI, and secure backend systems.", "icon": "code", "order": 1},
    {"title": "Penetration Testing", "description": "Comprehensive security assessments, vulnerability scanning, and ethical hacking services.", "icon": "shield", "order": 2},
    {"title": "Security Consulting", "description": "Architecture review, security best practices, compliance audits, and threat modeling.", "icon": "tool", "order": 3},
    {"title": "Cloud Security", "description": "Secure cloud architecture design, implementation, and monitoring on AWS, Azure, and GCP.", "icon": "cloud", "order": 4},
]
