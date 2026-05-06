# py-todo-list

A clean and functional Task Management web application built with **Django 6.0** and **Bootstrap 5**. This project demonstrates the core principles of Django, including Many-to-Many relationships, ORM queries, and the implementation of a RESTful-inspired interface for managing daily activities.

## 🌟 Key Features
*   **Task Management**: Full CRUD (Create, Read, Update, Delete) functionality for tasks.
*   **Tagging System**: Organize tasks using a Many-to-Many relationship with customizable tags.
*   **Smart Sorting**: Tasks are automatically ordered by completion status (active first) and creation date.
*   **Deadline Tracking**: Optional deadlines for tasks to help with time management.
*   **Responsive UI**: Styled with **Bootstrap 5** and **Django Crispy Forms** for a modern, mobile-friendly experience.
*   **Admin Dashboard**: Integrated Django Admin for easy data management.

## 🛠 Tech Stack
*   **Python 3.10+**
*   **Django 6.0.4**
*   **Crispy Forms (Bootstrap 5 pack)**
*   **Django Extensions** (for enhanced development workflow)
*   **SQLite** (Development database)

## 🏗 Database Schema
The project uses two core models to maintain a loosely coupled architecture:
*   **Task**: Handles content, timestamps, deadlines, and completion status.
*   **Tag**: A separate entity allowing for flexible task categorization.



## 📦 Installation & Setup

1. **Clone the repository:**
   ```bash
   git clone https://github.com/your-username/py-todo-list.git
   cd py-todo-list

2. **Set up a virtual environment:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # Windows: venv\Scripts\activate
   
3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt

4. **Run migrations:**
   ```bash
   python manage.py migrate
   
5. **Create a Superuser:**
   ```bash
   python manage.py createsuperuser

6. **Start the development server:**
   ```bash
   python manage.py runserver
   
Access the app at: http://127.0.0.1:8000/

Good luck and have a nice day!
