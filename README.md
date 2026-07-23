# Job Application Tracker

A Django web app for tracking job applications — built to practice Forms,
CRUD operations, template inheritance, and custom middleware.

## Features

- **Home dashboard** — total applications and a breakdown by status
  (Applied, Interview, Offer, Accepted, Rejected).
- **Full CRUD** on job applications: create, list, view detail, edit, delete
  (with a confirmation page before delete).
- **Validated ModelForm**:
  - Company name and position are required.
  - Salary cannot be negative.
  - Deadline cannot be earlier than the application date.
  - Notes cannot exceed 500 characters.
  - Errors render below the relevant field.
- **Template inheritance** — `base.html` with `navbar.html` and `footer.html`
  included, Bootstrap 5 styling, and success messages after
  create/update/delete.
- **Custom middleware** (`RequestLoggerMiddleware`) that logs the time,
  HTTP method, and path of every request to the console.

## Project structure

```
job_tracker/
├── job_tracker/        # project settings, root urls
├── jobs/                # app: models, forms, views, urls, middleware, admin
├── templates/
│   ├── base.html
│   ├── navbar.html
│   ├── footer.html
│   ├── home.html
│   └── jobs/
│       ├── list.html
│       ├── create.html
│       ├── update.html
│       ├── delete.html
│       ├── detail.html
│       └── _form_fields.html   # shared form partial for create/update
├── static/
│   ├── css/style.css
│   └── js/main.js
├── manage.py
└── requirements.txt
```

## URLs

| URL                  | View                     |
|-----------------------|--------------------------|
| `/`                  | Home dashboard           |
| `/jobs/`             | List all applications    |
| `/jobs/add/`         | Add a new application    |
| `/jobs/<id>/`        | View application detail  |
| `/jobs/<id>/edit/`   | Edit an application      |
| `/jobs/<id>/delete/` | Confirm & delete         |

## Setup

```bash
python3 -m venv venv
source venv/bin/activate        # venv\Scripts\activate on Windows
pip install -r requirements.txt

python3 manage.py migrate
python3 manage.py createsuperuser   # optional, for /admin/
python3 manage.py runserver
```

Visit `http://127.0.0.1:8000/` in your browser.

Every request is logged to the console by `RequestLoggerMiddleware`, e.g.:

```
---------------------------------
Time   : 2026-07-22 10:45 AM
Method : GET
Path   : /jobs/
---------------------------------
```

## Tech

- Python / Django
- SQLite (default dev database)
- Bootstrap 5 (via CDN)
