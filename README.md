# M Hasan - Portfolio

Full Stack Developer & Cybersecurity Expert Portfolio — **Astro.js** + **FastAPI** + **MongoDB**.

## 🚀 Tech Stack
- **Frontend:** Astro.js on Cloudflare Pages
- **Backend:** FastAPI on Render
- **Database:** MongoDB Atlas (free tier)

## 🌐 After Deployment
- **Frontend:** https://portfolio.pages.dev
- **Backend:** https://portfolio-api.onrender.com
- **API Docs:** https://portfolio-api.onrender.com/docs

---

## 🚀 Deploy Step-by-Step

### 1️⃣ MongoDB Atlas
1. Go to [MongoDB Atlas](https://cloud.mongodb.com) → Create free cluster
2. **Network Access** → Add IP `0.0.0.0/0`
3. **Database Access** → Create user, save credentials
4. **Connect** → Drivers → Copy connection string (`mongodb+srv://...`)

### 2️⃣ Render (Backend)
1. Push repo to GitHub → [Render](https://render.com) → New Web Service
2. **Root Directory:** `backend`
3. **Build:** `pip install -r requirements.txt`
4. **Start:** `uvicorn app.main:app --host 0.0.0.0 --port $PORT`
5. **Env vars:**
   - `MONGO_URI` ← your Atlas connection string
   - `MONGO_DB` → `portfolio_db`
   - `SECRET_KEY` → (generate random)
   - `ADMIN_USERNAME` → `admin`
   - `ADMIN_PASSWORD` → (pick a secure one)

### 3️⃣ Cloudflare Pages (Frontend)
1. [Cloudflare Pages](https://pages.cloudflare.com) → Create project → Connect repo
2. **Framework:** Astro
3. **Build:** `cd frontend && npm install && npm run build`
4. **Output:** `frontend/dist`
5. Deploy → Get `https://portfolio.pages.dev`

### 4️⃣ Connect Frontend ↔ Backend
After deploying, edit `frontend/src/layouts/Layout.astro` and update the Render URL, then redeploy Cloudflare Pages:

```js
window.API_BASE = isDev ? 'http://localhost:8000' : 'https://portfolio-api.onrender.com';
```

---

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
