# Virtual HR – Smart Recruitment & HR Management System

<p align="center">
  <strong>A Full-Stack HR Management Application Built with FastAPI, React and SQLite</strong>
</p>

<p align="center">
  Simplifying recruitment workflows, candidate management, task tracking and interview scheduling through a centralized HR dashboard.
</p>

---

## 📌 Project Overview

**Virtual HR** is a full-stack web application designed to simplify and organize essential Human Resource (HR) and recruitment activities.

The application provides a centralized dashboard where HR teams can manage recruitment tasks, maintain candidate information, schedule interviews and monitor recruitment progress.

Built using **FastAPI, React.js, SQLAlchemy and SQLite**, the project demonstrates how modern frontend and backend technologies can work together to create a structured and scalable HR management solution.

The primary objective is to reduce manual HR operations, improve recruitment workflow visibility and organize candidate-related information in one place.

## 🎯 Project Objectives

- Centralize recruitment and HR activities.
- Simplify candidate information management.
- Organize and track HR tasks.
- Schedule and manage candidate interviews.
- Maintain recruitment status updates.
- Provide a user-friendly dashboard for HR operations.
- Demonstrate full-stack application development using Python and React.

## ✨ Key Features

### 1. HR Dashboard

- Centralized dashboard for HR operations.
- Organized sections for tasks and interviews.
- Clean and responsive user interface.
- Employer and Virtual HR demo-role selection.

### 2. Task Management

- Create new HR tasks.
- Add task descriptions.
- Assign tasks to team members.
- View all available tasks.
- Update task status.
- Delete completed or unnecessary tasks.

**Task statuses:**
- Pending
- In Progress
- Completed

### 3. Candidate Management API

The backend provides candidate management functionality to maintain recruitment records.

- Register new candidates.
- Store candidate details.
- Retrieve all registered candidates.
- View individual candidate information.
- Update recruitment status.
- Delete candidate records.
- Prevent duplicate candidate email registration.

**Candidate information includes:**

| Field | Description |
|---|---|
| Candidate ID | Unique candidate identifier |
| Candidate Name | Full name |
| Email | Email address |
| Phone | Contact number |
| Position | Applied job position |
| Experience | Years of experience |
| Status | Recruitment stage |
| Resume Link | Candidate resume reference |
| Notes | Additional information |

**Candidate recruitment statuses:**
- Applied
- Shortlisted
- Interview Scheduled
- Selected
- Rejected

### 4. Interview Scheduling

- Schedule candidate interviews.
- Associate an interview with a registered candidate.
- Store candidate name and email.
- Select interview date and time.
- Choose interview mode.
- View all scheduled interviews.
- View individual interview details.
- Update or reschedule interviews.
- Delete interview records.

**Available interview modes:**
- Voice
- Video
- Chat

When an interview is scheduled against a registered candidate, the backend automatically updates the candidate's recruitment status to **Interview Scheduled**.

*Note: Voice, Video and Chat currently represent interview scheduling modes. Actual video conferencing, voice calling and live chat functionality are not implemented.*

### 5. REST API Integration

The frontend communicates with the backend through REST APIs.

- FastAPI handles backend requests.
- React manages frontend interactions.
- Axios is used for API communication.
- SQLAlchemy manages database operations.
- SQLite stores application records.

### 6. Automatic Data Refresh

The dashboard uses periodic API polling to refresh task and interview information.

This provides near-real-time visibility, rather than WebSocket-based live updates.

---

## 🛠️ Technology Stack

| Technology | Purpose |
|---|---|
| Python | Backend programming |
| FastAPI | REST API development |
| React.js | Frontend development |
| JavaScript | Frontend functionality |
| SQLAlchemy | ORM and database operations |
| SQLite | Database storage |
| Pydantic | Data validation |
| Axios | API communication |
| HTML5 | Page structure |
| CSS3 | Styling and responsive design |
| Uvicorn | ASGI server |
| Swagger UI | API documentation and testing |
| Git & GitHub | Version control |

## 🏗️ System Architecture

```text
              USER
                |
                v
       REACT FRONTEND
          (Vite)
                |
                v
        AXIOS API CALLS
                |
                v
        FASTAPI BACKEND
                |
       ------------------
       |        |       |
       v        v       v
     TASKS  CANDIDATES INTERVIEWS
       |        |       |
       ------------------
                |
                v
          SQLALCHEMY
                |
                v
            SQLITE
```

## 📂 Project Structure

```text
Virtual HR/
│
├── BACKEND/
│   │
│   ├── routers/
│   │   ├── tasks.py
│   │   ├── interviews.py
│   │   └── candidates.py
│   │
│   ├── main.py
│   ├── database.py
│   ├── models.py
│   ├── schemas.py
│   ├── migrate_database.py
│   ├── salarite.db
│   └── requirements.txt
│
├── frontend/
│   │
│   ├── public/
│   ├── src/
│   │   ├── App.jsx
│   │   ├── App.css
│   │   ├── index.css
│   │   └── main.jsx
│   │
│   ├── index.html
│   ├── package.json
│   └── package-lock.json
│
└── README.md
```

*Note: The SQLite database file is named `salarite.db` internally in the current setup. The application branding is Virtual HR.*

## ⚙️ Installation and Setup

Follow these steps to run the project locally.

### Prerequisites

Install the following before starting:

- Python 3.10 or above
- Node.js and npm
- Visual Studio Code
- Git (optional)

### Step 1: Clone the Repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
```

Navigate into the project:

```bash
cd "Virtual HR"
```

### Step 2: Backend Setup

Navigate to the backend folder:

```bash
cd BACKEND
```

Create a virtual environment:

```bash
python -m venv venv
```

Activate the virtual environment in Windows PowerShell:

```powershell
.\venv\Scripts\Activate.ps1
```

Install backend dependencies:

```bash
pip install -r requirements.txt
```

Start the FastAPI server:

```bash
python -m uvicorn main:app --reload
```

Backend server:

```text
http://127.0.0.1:8000
```

### Step 3: Access API Documentation

Open the following URL in your browser:

```text
http://127.0.0.1:8000/docs
```

Swagger UI provides an interactive interface to test the available APIs.

### Step 4: Frontend Setup

Open another terminal and navigate to the frontend folder:

```bash
cd frontend
```

Install frontend dependencies:

```bash
npm install
```

Start the React development server:

```bash
npm run dev
```

Frontend application:

```text
http://localhost:5173
```

The frontend communicates with the backend running on port 8000.

---

## 🔗 API Endpoints

Base URL:

```text
http://127.0.0.1:8000
```

### Task Management APIs

| Method | Endpoint | Description |
|---|---|---|
| POST | `/tasks/` | Create a task |
| GET | `/tasks/` | Get all tasks |
| GET | `/tasks/{task_id}` | Get a specific task |
| PUT | `/tasks/{task_id}` | Update task status |
| DELETE | `/tasks/{task_id}` | Delete a task |

### Candidate Management APIs

| Method | Endpoint | Description |
|---|---|---|
| POST | `/candidates/` | Register a candidate |
| GET | `/candidates/` | Get all candidates |
| GET | `/candidates/{candidate_id}` | Get a specific candidate |
| PUT | `/candidates/{candidate_id}` | Update candidate status |
| DELETE | `/candidates/{candidate_id}` | Delete a candidate |

### Interview Scheduling APIs

| Method | Endpoint | Description |
|---|---|---|
| POST | `/interviews/` | Schedule an interview |
| GET | `/interviews/` | Get all interviews |
| GET | `/interviews/{interview_id}` | Get a specific interview |
| PUT | `/interviews/{interview_id}` | Update or reschedule interview |
| DELETE | `/interviews/{interview_id}` | Delete an interview |

### General APIs

| Method | Endpoint | Description |
|---|---|---|
| GET | `/` | Welcome endpoint |
| GET | `/health` | Application health check |

*All endpoints should be verified against the current backend implementation.*

---

## 🗄️ Database Design

Virtual HR uses SQLite as its database and SQLAlchemy as its Object Relational Mapper (ORM).

The application maintains three main database tables:

### 1. Tasks Table

Stores HR task information, including task title, description, assigned team member and task status.

### 2. Candidates Table

Stores candidate details, including contact information, applied position, experience and recruitment status.

### 3. Interviews Table

Stores interview information, including candidate details, interview date, interview mode and scheduling status.

The interviews table also supports a relationship with the candidates table through `candidate_id`.

## 🔄 Application Workflow

```text
          START
            |
            v
       OPEN DASHBOARD
            |
            v
       MANAGE HR TASKS
            |
            v
      REGISTER CANDIDATE
            |
            v
      STORE CANDIDATE DATA
            |
            v
      SCHEDULE INTERVIEW
            |
            v
     UPDATE CANDIDATE STATUS
            |
            v
       TRACK RECRUITMENT
            |
            v
            END
```

## 🔐 Validation and Error Handling

The backend uses Pydantic schemas and FastAPI exception handling to validate incoming requests.

Examples include:

- Required field validation.
- Email format validation.
- Candidate email uniqueness.
- Candidate existence checks before linked interview scheduling.
- Handling records that do not exist.
- Database rollback when interview creation fails.

## 🚀 Future Enhancements

The following improvements can make Virtual HR more powerful:

- Complete candidate management interface in React.
- Candidate selection dropdown in the interview scheduling form.
- Secure authentication and role-based access control.
- Separate employer and HR user accounts.
- Resume upload and document management.
- Email notifications for interview schedules.
- Interview reminders.
- Calendar integration.
- Actual video conferencing and live communication.
- Advanced recruitment analytics and reporting.
- WebSocket-based real-time updates.
- Cloud database integration.
- Docker-based deployment.
- Cloud hosting and production deployment.

## 📈 Learning Outcomes

Through this project, the following technical concepts are demonstrated:

- Full-stack web application development.
- REST API creation using FastAPI.
- React component-based development.
- Frontend and backend integration.
- Database design using SQLAlchemy.
- CRUD operations.
- Pydantic data validation.
- API testing through Swagger UI.
- Database relationships and foreign keys.
- Application structure and modular programming.

## 👩‍💻 Developer

**Aakansha Saxena**

MCA Student | Python | Data Science | Machine Learning | Full-Stack Development

## ⭐ Support

If you find this project interesting, consider giving it a ⭐ on GitHub.

---

<p align="center">
  <strong>Virtual HR</strong><br/>
  Smart Recruitment. Organized Workflows. Better HR Management.
</p>
