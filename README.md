# M Hasan - Portfolio

Full Stack Developer & Cybersecurity Expert Portfolio — **Astro.js** + **JSON**.

## 🚀 Tech Stack

- **Frontend:** Astro.js
- **Data:** JSON files (build-time) + localStorage (dashboard edits)

## 🛠️ Getting Started

### Prerequisites

- Node.js 18+

### Start Development

```bash
cd frontend
npm install
npm run dev
```

Portfolio: http://localhost:4321

### Login

**Username:** `admin`
**Password:** `admin123`

## 📋 Dashboard (http://localhost:4321/dashboard/login)

All CRUD operations save to **localStorage** — changes persist in your browser only.
To make permanent changes, update the JSON files in `frontend/src/data/` and rebuild.

- **Homepage** — Edit hero text, stats, section titles
- **Projects** — Add/edit/delete portfolio projects
- **Services** — Add/edit/delete homepage services
- **Skills** — Add/edit/delete technical skills
- **Avatar** — Upload profile photo (saved as data URL)
- **Settings** — Profile info & social links

## 📁 Data Files

Edit `frontend/src/data/` to update site content permanently:

| File            | Content                      |
| --------------- | ---------------------------- |
| `profile.json`  | Personal info & social links |
| `homepage.json` | Hero section, stats, titles  |
| `projects.json` | Portfolio projects           |
| `skills.json`   | Technical skills             |
| `services.json` | Services offered             |
| `auth.json`     | Admin credentials            |

## 🏗️ Build

```bash
cd frontend
npm run build
npm run preview
```
