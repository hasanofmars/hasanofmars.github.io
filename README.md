# M Hasan - Portfolio

Full Stack Developer & Cybersecurity Expert Portfolio — **Astro.js** + **FastAPI** + **MongoDB**.

## 🚀 Tech Stack

- **Frontend:** Astro.js
- **Backend:** FastAPI
- **Database:** MongoDB

## 🛠️ Getting Started

### Prerequisites

- Python 3.10+
- Node.js 18+
- MongoDB (running locally on port 27017)

### 1️⃣ Start Backend

```bash
cd backend
pip install -r requirements.txt
python seed.py
python -m uvicorn app.main:app --reload --port 8000
```

API docs: http://localhost:8000/docs

### 2️⃣ Start Frontend

```bash
cd frontend
npm install
npm run dev
```

Portfolio: http://localhost:4321

### 3️⃣ Login

**Username:** `admin`
**Password:** `admin123`

## 📋 Dashboard (http://localhost:4321/dashboard/login)

- **Homepage** — Edit hero text, stats, section titles
- **Projects** — Add/edit/delete portfolio projects
- **Services** — Add/edit/delete homepage services
- **Avatar** — Upload profile photo
- **Settings** — Profile info & social links

## 🛠️ Local Dev

**Backend:** `cd backend && pip install -r requirements.txt && python seed.py && python -m uvicorn app.main:app --reload --port 8000`
**Frontend:** `cd frontend && npm install && npm run dev`
**Login:** `admin` / `admin123`

## 📋 Dashboard

- **Homepage** — Edit hero, stats, titles
- **Projects** — CRUD portfolio projects
- **Services** — CRUD homepage services
- **Avatar** — Upload profile photo
- **Settings** — Profile & social links
