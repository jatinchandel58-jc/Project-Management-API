# Project Management API

A backend REST API for managing users, workspaces, projects, tasks, comments, attachments, and notifications.

Built with **Python, Django, Django REST Framework, PostgreSQL, and JWT Authentication**.

## 🚀 Features

* User registration and login
* JWT-based authentication
* Access and refresh tokens
* Logout with refresh-token blacklisting
* User profile management
* Password change
* Profile picture upload
* Workspace management
* Workspace member management
* Project management
* Project status management
* Task management
* Task assignment
* Task filtering and searching
* Comments
* File attachments
* Notifications
* PostgreSQL database
* RESTful API architecture
* Permission-based access control

---

## 🛠️ Technologies Used

* **Python**
* **Django**
* **Django REST Framework**
* **PostgreSQL**
* **Simple JWT**
* **Django Filter**
* **Git & GitHub**
* **Postman**
* **Docker** (optional/deployment ready)

---

## 📁 Project Structure

```text
Project Management API/
│
├── core/
│   ├── accounts/
│   ├── workspace/
│   ├── projects/
│   ├── tasks/
│   ├── comments/
│   ├── attachments/
│   ├── notifications/
│   │
│   ├── manage.py
│   └── ...
│
├── .env
├── .gitignore
├── requirements.txt
└── README.md
```

---

## 🔐 Authentication

The API uses **JWT (JSON Web Token)** authentication.

### Register

```http
POST /api/register/
```

Example request:

```json
{
    "first_name": "Jatin",
    "last_name": "Chandel",
    "email": "jatin@example.com",
    "password": "Admin123!"
}
```

### Login

```http
POST /api/login/
```

The login endpoint returns an access token and refresh token.

### Refresh Token

```http
POST /api/token/refresh/
```

### Logout

```http
POST /api/logout/
```

The refresh token is blacklisted after logout.

---

# 👤 User & Profile

Users can:

* Register
* Login
* View their profile
* Update their profile
* Upload a profile picture
* Change their password
* Logout

Example:

```http
GET /api/profile/
```

Authenticated requests should include:

```http
Authorization: Bearer <access_token>
```

---

# 🏢 Workspace Management

A workspace allows multiple users to collaborate on projects and tasks.

Main functionality:

* Create workspace
* View workspace
* Update workspace
* Delete workspace
* Add workspace members
* Manage workspace members

Example:

```http
GET /api/workspace/
```

Add a member:

```http
POST /api/workspace/member/
```

---

# 📋 Project Management

Projects belong to a workspace and can have different statuses.

### Project statuses

* `planning`
* `in_progress`
* `completed`
* `on_hold`

Example:

```http
GET /api/projects/
```

Create project:

```http
POST /api/projects/
```

Example:

```json
{
    "name": "E-Commerce API",
    "description": "Backend API for an e-commerce application",
    "status": "planning",
    "start_date": "2026-08-25",
    "end_date": "2026-09-25"
}
```

The API validates project dates and ensures that users can only access projects they are allowed to manage.

---

# ✅ Task Management

Tasks belong to projects and can be assigned to workspace members.

Features include:

* Create task
* View tasks
* Update task
* Delete task
* Assign task to a member
* Filter tasks
* Search tasks
* Validate task due dates
* Permission-based task visibility

### Task access rules

* Workspace owners can view all workspace tasks.
* Workspace members can view tasks assigned to them.
* Only valid workspace members can be assigned to tasks.

Example:

```http
GET /api/tasks/
```

Create task:

```http
POST /api/tasks/
```

Example:

```json
{
    "title": "Create Authentication API",
    "description": "Implement JWT authentication",
    "project": 1,
    "assigned_to": 2,
    "due_date": "2026-09-01"
}
```

---

# 💬 Comments

Users can add comments to tasks or projects.

Example:

```http
POST /api/comments/
```

Example request:

```json
{
    "task": 1,
    "content": "Authentication API has been completed."
}
```

---

# 📎 Attachments

The API supports uploading files related to tasks/projects.

For file uploads, use:

```text
Content-Type: multipart/form-data
```

Example:

```http
POST /api/attachments/
```

---

# 🔔 Notifications

The project includes a notification system for important events.

Django Signals can be used to automatically create notifications when specific events occur.

For example:

```text
Task Created
     ↓
post_save Signal
     ↓
Notification Created
```

---

# 🔎 Search & Filtering

The API supports searching and filtering where applicable.

Example:

```http
GET /api/workspace/?q=development
```

Filtering can be performed using query parameters.

---

# 🗄️ Database

The project uses **PostgreSQL** as the primary database.

Database configuration is stored using environment variables.

Example:

```env
DB_NAME=project_management
DB_USER=postgres
DB_PASSWORD=your_password
DB_HOST=127.0.0.1
DB_PORT=5432
```

> Never commit your actual `.env` file or database password to GitHub.

---

# ⚙️ Installation & Setup

## 1. Clone the repository

```bash
git clone https://github.com/jatinchandel58-jc/Project-Management-API.git
```

Move into the project:

```bash
cd Project-Management-API
```

---

## 2. Create a virtual environment

Windows:

```bash
python -m venv venv
```

Activate it:

```bash
venv\Scripts\activate
```

---

## 3. Install dependencies

```bash
pip install -r requirements.txt
```

---

## 4. Configure environment variables

Create a `.env` file and add your database configuration:

```env
DB_NAME=project_management
DB_USER=postgres
DB_PASSWORD=your_password
DB_HOST=127.0.0.1
DB_PORT=5432
```

---

## 5. Run migrations

```bash
python manage.py makemigrations
```

```bash
python manage.py migrate
```

---

## 6. Create a superuser

```bash
python manage.py createsuperuser
```

---

## 7. Start the development server

```bash
python manage.py runserver
```

The API will be available at:

```text
http://127.0.0.1:8000/
```

---

# 🧪 Testing API

The API can be tested using **Postman**.

Basic workflow:

```text
Register
   ↓
Login
   ↓
Get Access Token
   ↓
Create Workspace
   ↓
Add Members
   ↓
Create Project
   ↓
Create Task
   ↓
Assign Task
   ↓
Add Comments / Attachments
```

For protected endpoints, send:

```http
Authorization: Bearer <access_token>
```

---

# 🔑 Example API Flow

### 1. Register

```http
POST /api/register/
```

### 2. Login

```http
POST /api/login/
```

### 3. Create Workspace

```http
POST /api/workspace/
```

### 4. Add Member

```http
POST /api/workspace/member/
```

### 5. Create Project

```http
POST /api/projects/
```

### 6. Create Task

```http
POST /api/tasks/
```

### 7. Add Comment

```http
POST /api/comments/
```

### 8. Upload Attachment

```http
POST /api/attachments/
```

---

# 🔒 Security

The project follows several security practices:

* JWT authentication
* Password validation
* Permission-based access
* Refresh-token blacklisting
* Environment variables for sensitive configuration
* `.gitignore` for sensitive/local files

The following files should not be committed:

```text
.env
db.sqlite3
venv/
.vscode/
```

---

# 📌 Future Improvements

Possible future improvements include:

* Email notifications
* Real-time notifications using WebSockets
* Task priority
* Task labels/tags
* Project dashboards
* Activity history
* Advanced reporting
* Redis caching
* Celery background tasks
* Docker deployment
* API documentation with Swagger/OpenAPI

---

# 👨‍💻 Author

**Jatin Chandel**

Backend Developer | Python | Django | Django REST Framework | PostgreSQL

---

# 📄 License

This project is created for learning and portfolio purposes.
