# Todo List Application – Flask

A simple Task Management Web Application built with **Python Flask**. This project is designed to practice Backend Development, RESTful principles, database integration, and software development best practices.

## 1. Project Overview

Todo List is a web application that allows users to manage their daily tasks efficiently.

Users can create, view, update, delete, and track the completion status of their tasks through a simple web interface.

**Project Status:** In Development

## 2. Project Objectives

The main objectives of this project are:

- Understand Flask fundamentals and application structure.
- Practice HTTP Methods and request/response handling.
- Implement CRUD operations.
- Understand ORM and database interactions.
- Learn how to organize a maintainable Flask application.
- Practice backend development workflows.

## 3. Technology Stack

| Technology | Purpose |
|---|---|
| Python | Programming language |
| Flask | Backend web framework |
| Flask-SQLAlchemy | ORM and database management |
| SQLite | Relational database |
| HTML5 | Web page structure |
| CSS3 | Web page styling |
| Bootstrap | Responsive UI components |
| Jinja2 | Template rendering |
| Git | Version control |

## 4. Core Features

### Task Management (CRUD)

- **Create Task:** Add a new task.
- **Read Tasks:** Display all existing tasks.
- **Update Task:** Edit task information.
- **Delete Task:** Remove a task.
- **Complete Task:** Mark a task as completed or pending.

### Task Organization

- Filter tasks by status.
- Search tasks by title.
- Display task creation timestamps.

### Future Features

- User Registration and Login.
- User Authentication and Authorization.
- Personal task management.
- RESTful API.
- PostgreSQL integration.

## 5. System Architecture

The application follows a simple three-layer architecture:

```text
Client (Browser)
       |
       | HTTP Request
       v
Flask Application
       |
       +---- Routes
       |
       +---- Business Logic
       |
       +---- SQLAlchemy ORM
                  |
                  v
             SQLite Database
                  |
                  v
             HTTP Response
                  |
                  v
             Client (Browser)
```

## 6. Project Structure

```text
TodoList/
│
├── app/
│   ├── __init__.py
│   ├── routes.py
│   │
│   ├── templates/
│   │   └── index.html
│   │
│   └── static/
│       └── style.css
│
├── config.py
├── run.py
├── requirements.txt
├── .gitignore
└── README.md
```

### Directory Description

| File / Directory | Description |
|---|---|
| `app/` | Main application package |
| `__init__.py` | Flask application initialization |
| `routes.py` | Application routes and request handling |
| `templates/` | HTML templates |
| `static/` | CSS, JavaScript, and static assets |
| `config.py` | Application configuration |
| `run.py` | Application entry point |
| `requirements.txt` | Python dependencies |
| `.gitignore` | Files excluded from Git |

## 7. Installation and Setup

### Prerequisites

- Python 3.10+
- pip
- Git

### Step 1: Clone the repository

```bash
git clone <repository-url>
cd TodoList
```

### Step 2: Create a virtual environment

```bash
py -3 -m venv .venv
```

### Step 3: Activate virtual environment

Windows PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

Linux / macOS:

```bash
source .venv/bin/activate
```

### Step 4: Install dependencies

```bash
python -m pip install -r requirements.txt
```

### Step 5: Run the application

```bash
python run.py
```

Open your browser:

```text
http://127.0.0.1:5000/
```

## 8. HTTP Methods

The application uses HTTP methods to handle task operations.

| Method | Endpoint | Description |
|---|---|---|
| GET | `/` | Display task list |
| GET | `/tasks/<id>` | Get task details |
| POST | `/tasks` | Create a new task |
| PUT | `/tasks/<id>` | Update an entire task |
| PATCH | `/tasks/<id>` | Update part of a task |
| DELETE | `/tasks/<id>` | Delete a task |

*Note: These are the planned API-style endpoints. The actual implementation may use Flask form submissions and redirects for the server-rendered web interface.*

## 9. Development Roadmap

- [ ] Phase 1: Project Setup
  - [ ] Create virtual environment.
  - [ ] Install Flask.
  - [ ] Set up project structure.
  - [ ] Implement Flask Application Factory.
  - [ ] Configure Blueprint.

- [ ] Phase 2: Flask Fundamentals
  - [ ] Understand routing.
  - [ ] Handle HTTP requests and responses.
  - [ ] Integrate Jinja2 templates.
  - [ ] Handle HTML forms.

- [ ] Phase 3: Database Integration
  - [ ] Configure Flask-SQLAlchemy.
  - [ ] Create Task model.
  - [ ] Understand ORM.
  - [ ] Implement database operations.

- [ ] Phase 4: CRUD Implementation
  - [ ] Create tasks.
  - [ ] Display tasks.
  - [ ] Update tasks.
  - [ ] Delete tasks.
  - [ ] Complete tasks.

- [ ] Phase 5: Application Improvements
  - [ ] Input validation.
  - [ ] Error handling.
  - [ ] Search and filtering.
  - [ ] Unit testing.

- [ ] Phase 6: Advanced Features
  - [ ] User authentication.
  - [ ] PostgreSQL integration.
  - [ ] RESTful API.
  - [ ] Dockerize application.
  - [ ] Deploy application.

## 10. Learning Outcomes

By completing this project, the developer expects to gain practical experience in:

- Python programming and OOP.
- Flask framework and application architecture.
- HTTP protocol and REST API concepts.
- SQL and relational database management.
- ORM with SQLAlchemy.
- Backend application development.
- Git version control and project organization.
- Basic testing and deployment.

---

**Author:** Minh Duong  
**Project:** Todo List Application  
**Backend Framework:** Flask  
**Language:** Python