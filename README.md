# Online Course Enrollment API

A simple Django REST API that allows users to browse courses, enroll in courses, and manage their enrollments.

---

## ⚙️ Project Overview

This API provides:

- CRUD operations for **Users**
- CRUD operations for **Courses**
- Endpoints for **enrolling** and **unenrolling** from courses
- Endpoints to view:
  - All courses a user is enrolled in
  - All students enrolled in a specific course

---

## 🏗️ Tech Stack

- Python  
- Django  
- Django REST Framework  
- SQLite (default)  
- Git & GitHub  
- PythonAnywhere or Heroku (deployment)

---

## 📌 Features

### Users
- Create, update, delete users  
- View all users or one user  

### Courses
- Create, update, delete courses  
- Search courses  
- View course details  

### Enrollments
- Enroll in a course  
- Unenroll from a course  
- View a user's enrolled courses  
- View students in a course  

---

## 📁 Project Structure

online-course-api/
│── api/
│ ├── migrations/
│ ├── models.py
│ ├── serializers.py
│ ├── views.py
│ ├── urls.py
│── online_course_api/
│ ├── settings.py
│ ├── urls.py
│── manage.py


---

## 🚀 API Endpoints

### Users
| Method | Endpoint | Description |
|-------|----------|-------------|
| POST | /users/ | Create user |
| GET | /users/ | List users |
| GET | /users/{id}/ | Retrieve user |
| PUT/PATCH | /users/{id}/ | Update user |
| DELETE | /users/{id}/ | Delete user |

### Courses
| Method | Endpoint | Description |
|-------|----------|-------------|
| POST | /courses/ | Create course |
| GET | /courses/ | List courses |
| GET | /courses/{id}/ | Course details |
| PUT/PATCH | /courses/{id}/ | Update course |
| DELETE | /courses/{id}/ | Delete course |
| GET | /courses/search/?q={keyword} | Search courses |

### Enrollments
| Method | Endpoint | Description |
|-------|----------|-------------|
| POST | /enroll/ | Enroll a user |
| POST | /unenroll/ | Unenroll user |
| GET | /users/{id}/courses/ | User's courses |
| GET | /courses/{id}/students/ | Students in course |

---

## 📄 License

This project is open-source and free to use.
