# Django Blog Practice

A practice blog application built while learning Django web development.

## About This Project

This is a learning project created as part of my journey to become proficient in full-stack web development. The project follows along with a Django course to understand core concepts including:

- Django project structure
- URL routing and views
- Template rendering
- Database models (upcoming)
- User authentication (upcoming)

## Technologies Used

- **Python** 3.11
- **Django** 5.2
- **SQLite** (database)

## Current Status

**In Progress** - Actively learning and building out features as I progress through the course.

## Setup Instructions

If you want to run this project locally:

1. Clone the repository
   ```bash
   git clone https://github.com/YOUR_USERNAME/django-blog-practice.git
   cd django-blog-practice
   ```

2. Create a virtual environment
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies (once requirements.txt is added)
   ```bash
   pip install django
   ```

4. Run migrations
   ```bash
   python manage.py migrate
   ```

5. Start the development server
   ```bash
   python manage.py runserver
   ```

6. Visit `http://localhost:8000` in your browser

## Learning Goals

By completing this project, I aim to:
- Understand Django's MVT (Model-View-Template) architecture
- Build dynamic web applications with Python
- Work with databases using Django's ORM
- Implement user authentication and authorization
- Deploy a Django application (future goal)

## Future Plans

- Add blog post creation and management
- Implement user accounts and authentication
- Add comments system
- Style with CSS/Bootstrap
- Deploy to a hosting platform

##Security note 

- Earlier commits included a hard-coded SECRET_KEY during learning. It’s now rotated and loaded from environment variables.

---

*This is a practice project created for learning purposes as I work toward becoming employable in web development by Easter 2026.*
