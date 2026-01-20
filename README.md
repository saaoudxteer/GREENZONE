# GREENZONE — Eco-Friendly Stays Booking Platform (Airbnb-like) | Django

GREENZONE is a Django web application inspired by Airbnb, focused on **eco-friendly accommodations**.  
The idea is simple: help users book greener stays, and (as the product direction) make each booking contribute to sustainable actions (reforestation, renewable energy projects, etc.).

This repository contains the full application: backend, templates, static assets, and a clean project structure split into domains (accounts / accommodations / bookings).

---

## What I built (project scope)

### 1) Core platform structure (Django)
I built the project as a classic Django app, with a modular structure:

- `accounts/` — authentication & user-related pages
- `accommodations/` — eco stays (listing + details + images + metadata)
- `bookings/` — reservation flow (creating bookings and storing booking data)
- `config/` — global Django configuration (settings, urls, wsgi/asgi)

This separation keeps the codebase easier to maintain and makes features evolve without mixing concerns.

### 2) Accommodation listings + booking flow
The application includes:
- Accommodation pages (browse + detail view)
- A booking workflow connected to accommodations
- Django Admin compatibility to manage data

### 3) Media / images
Accommodation images are supported using Django’s media system and Pillow.

### 4) Reproducible setup (professional Git hygiene)
I cleaned the repository to avoid committing local/dev artifacts and made the project reproducible:
- No committed virtual environments / IDE files / local DB state
- Configuration through environment variables (`python-decouple`)
- Dependencies pinned in `requirements.txt`
- `.env.example` provided so the project can be started quickly without guessing variables

### 5) CI (GitHub Actions)
I set up a GitHub Actions CI pipeline to enforce correctness on every push/PR:
- install dependencies
- generate `.env` from `.env.example`
- `python manage.py check`
- ensure migrations are not missing (`makemigrations --check --dry-run`)
- run migrations
- run tests

This ensures the repo stays “clone and run” and prevents migration drift.

---

## Tech Stack
- **Backend:** Django (Python)
- **Frontend:** Django templates (server-rendered HTML)
- **Database (dev):** SQLite
- **Server (prod):** Gunicorn
- **Config:** python-decouple
- **Images:** Pillow
- **CI:** GitHub Actions

---

## Getting Started (Local)

### Requirements
- Python 3.11+
- pip

### Setup
```bash
git clone https://github.com/saaoudxteer/GREENZONE.git
cd GREENZONE

python -m venv .venv
source .venv/bin/activate

pip install -r requirements.txt
cp .env.example .env

python manage.py migrate
python manage.py createsuperuser
python manage.py runserver

