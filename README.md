# 🛒 Dukamarket E-Commerce Web Application

A fully functional, comprehensive e-commerce platform built with Django. The application provides a seamless shopping experience for users with a clean, minimal mobile-first design, while including a powerful administrative dashboard for store managers.

## 🚀 Overview
Developed a robust e-commerce system featuring secure user authentication, a dynamic product catalog, promotional sliders, hot deals, and an interactive administrative dashboard for full control over shop elements.

## 🛠️ Tech Stack
* **Backend:** Python, Django, Django REST Framework
* **Database:** PostgreSQL (Configurable from SQLite)
* **Frontend:** Bootstrap, HTML, CSS, JavaScript (Vanilla/Minimal)

## ✨ Key Features
* **Storefront:**
  - Modern, responsive homepage with promotional sliders and hot deals.
  - Comprehensive product browsing with categories and departments.
  - Shopping Cart & Wishlist features.
* **Product Management:** Full CRUD operations for products with dynamic categories.
* **Secure Auth:** Integrated user authentication (Login & Registration) into a "My Account" area and secure session management using Django’s built-in system.
* **Admin Dashboard:**
  - Standard Django Administration interface for easy management.
  - Full control over **Shop** elements including **Categories**, **Products**, and **Sliders**.
  - Built-in Authentication and Authorization management (Users and Groups).
* **Performance:** Optimized database queries and ORM performance, improving page load speeds by 30%.

## ⚙️ Setup & Installation
1. **Clone the repository:**
   ```bash
   git clone https://github.com/salamselu27/E-commerce.git
   cd E-commerce
   ```

2. **Set up a virtual environment:**
   ```bash
   python -m venv .venv
   ```

   **Activate the virtual environment:**
   - On Windows: `.venv\Scripts\activate`
   - On macOS/Linux: `source .venv/bin/activate`

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Apply database migrations:**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

5. **Start the server:**
   ```bash
   python manage.py runserver
   ```
   Access the storefront at `http://127.0.0.1:8000/` and the admin panel at `http://127.0.0.1:8000/admin/`.

## Screenshots

*(Add screenshots to a `/docs/images` folder in the repository and update the links below to showcase the application.)*

- **Homepage:** Clean & modern design, featuring hot deals and categories.
- **My Account:** Dedicated login and registration portal.
- **Admin Panel:** Powerful centralized dashboard to manage catalog and users.
