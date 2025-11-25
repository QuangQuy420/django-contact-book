# 📖 Django Contact Book

A simple Django application that manages **Contacts** and **Groups**, demonstrates **CRUD operations**, **Many-to-Many relationships**, and **database transactions**.  
Built for learning **Django ORM**, project structure, Git branching, and full-stack workflows.

---

## ✨ Features

- Create, Read, Update, Delete **Contacts**
- Create, Read, Update, Delete **Groups**
- Contacts can belong to multiple groups (**Many-to-Many**)
- Transactional operations using `transaction.atomic()`
- Django Admin dashboard for easy management
- SQLite database (default)

---

## 🛠 Requirements

- Python **3.12+** (recommended via pyenv)
- Django **5+**
- Git
- VS Code or PyCharm

---

## 🚀 Installation & Setup

### 1. Clone the repository

```bash
git clone git@github.com:YOUR_USERNAME/django-contact-book.git
cd django-contact-book
```

### 2. Create virtual environment

```bash
python -m venv .venv
source .venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

If you don’t have `requirements.txt` yet:

```bash
pip freeze > requirements.txt
```

---

## 🗄 Database Setup

### Apply migrations

```bash
python manage.py migrate
```

### Create admin user

```bash
python manage.py createsuperuser
```

---

## ▶ Running the Application

### Start server

```bash
python manage.py runserver
```

### Access

- App: http://localhost:8000  
- Admin: http://localhost:8000/admin

---

## 📁 Project Structure

```
django-contact-book/
├── config/
├── contacts/
│   ├── migrations/
│   ├── templates/
│   │   └── contacts/
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   ├── admin.py
├── db.sqlite3
├── manage.py
├── README.md
└── requirements.txt
```
