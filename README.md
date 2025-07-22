# 📝 Blogger – Django Blog Platform

A simple and elegant blog platform built with Django. This project showcases core web development features like creating, editing, and displaying blog posts with support for user comments, authentication, and responsive design.

---

![Django](https://img.shields.io/badge/Django-5.x-green?logo=django)
![Python](https://img.shields.io/badge/Python-3.12-blue?logo=python)
![Bootstrap](https://img.shields.io/badge/Bootstrap-5-purple?logo=bootstrap)
![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)

---

## 🖼️ Preview

<p align="center">
  <img src="homepage1.png" alt="Homepage Screenshot" width="48%">
  <img src="homepage2.png" alt="Post Detail Screenshot" width="48%">
</p>

---

## 🚀 Features

-  Create, update, and delete blog posts (CRUD)
-  User registration, login, and logout
-  Each user can manage their own posts
-  Add, edit, and delete comments on posts
-  Filter posts by category or author
-  Automatically display latest posts and comments
-  Responsive and clean UI using Bootstrap 5
-  Organized views using Django class-based views (CBVs)
-  Admin panel with full control over posts, users, and comments
-  Custom static files (CSS + JS)
-  CSRF protection and form validation
-  Integrated post detail pages with clean layout

---

## 🧰 Tech Stack

- **Framework:** Django 5.x
- **Language:** Python 3.12
- **Frontend:** HTML, Bootstrap 5
- **Forms:** Django Crispy Forms (Bootstrap5)
- **Database:** SQLite3

---

## 🛠️ Getting Started

1. **Clone the repo**
   ```bash
   git clone https://github.com/Shahad-Almalki/NewBlogger.git
   cd NewBlogger/src

2. **Create & activate virtual environment**
   ```bash
   python -m venv env
   env\Scripts\activate

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt

4. **Apply migrations & run**
   ```bash
   python manage.py migrate
   python manage.py runserver


5. **Folder Structure**
  <pre> ```bash src/ ├── blog/ # Blog app ├── user/ # User registration & login ├── templates/ # HTML templates ├── static/ # CSS, JS, images ├── manage.py # Django project entry point ├── README.md # Project documentation └── requirements.txt# Dependencies ``` </pre>
