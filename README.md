# Student Team Formation System

## 📌 Overview

The Student Team Formation System is a full-stack web application that automates the process of forming balanced student teams using **K-Means clustering techniques**. It groups students based on skills, preferences, and attributes to ensure fair and efficient team formation.

The system also includes secure authentication, OTP verification, project upload functionality, and separate dashboards for students and admins.

---

## 🚀 Features

### 👩‍🎓 Student Module

* Student registration and login
* OTP-based email verification
* Profile management
* Upload projects (PDF, ZIP, images, etc.)
* View assigned teams
* Participate in hackathon events

---

### 🛠️ Admin Module

* Admin login dashboard
* Manage student records
* View system activity
* Create hackathons
* Edit hackathons
* Delete hackathons
* View all formed teams
* Assign and monitor teams

---

## 🤖 Core Functionality

* Data preprocessing of student information
* K-Means clustering for grouping students
* Role assignment within teams (Project manager, Frontend developer, Backend developer, Communication lead)
* Automated balanced team generation
* Secure authentication system (OTP + password hashing)

---

## 🔄 Workflow

1. User Registration
2. OTP Verification
3. Login Authentication
4. Data Collection (skills, preferences, projects)
5. K-Means Clustering
6. Role Assignment
7. Team Formation
8. Final Output Display

---

## 🧠 Tech Stack

### Backend

* Python (Flask)
* Oracle / SQL Database

### Frontend

* HTML
* CSS
* JavaScript
* Jinja2 Templates

### Machine Learning

* K-Means Clustering

### Security

* OTP Email Verification (SMTP)
* Password Hashing (Werkzeug)

### File Handling

* Project upload system
* Supports PDF, ZIP, Image files

---

## 📂 Project Structure

```text
student-team-formation-system/
│
├── backend/                 # Core backend logic
│   ├── clustering.py        # K-Means clustering logic
│   ├── db_connection.py     # Database connection setup
│   ├── insert_students.py   # Insert student data into DB
│   ├── role_assignment.py   # Assign roles to team members
│   ├── team_formation.py    # Team generation logic
│   ├── teamup(1).csv        # Dataset
│
├── static/                  # CSS files
│   └── style.css
│
├── templates/               # HTML pages (Flask UI)
│   ├── admin_dash.html
│   ├── admin_login.html
│   ├── login.html
│   ├── signup.html
│   ├── dashboard.html
│   ├── teams.html
│   ├── hackathon_events.html
│   ├── student_management.html
│   ├── view_profile.html
│   └── ...
│
├── app.py                  # Main Flask application
├── fix_db.py               # Database setup/repair script
├── requirements.txt        # Project dependencies
├── .gitignore
└── README.md
```

---

## ▶️ How to Run the Project

```bash
git clone https://github.com/your-username/student-team-formation-system.git
cd student-team-formation-system
pip install -r requirements.txt
python app.py
```

Open in browser:

```
http://127.0.0.1:5000/
```

---

## 📊 Output

* Student registration and login system
* OTP verification system
* Project upload feature
* Admin dashboard with full control
* Automated team formation using K-Means clustering
* Role-based team assignment
* Hackathon management system

---

## 🎯 Key Learning Outcomes

* Full-stack web development using Flask
* Database integration (Oracle/SQL)
* Machine learning concept (K-Means clustering)
* Authentication and security systems
* Real-world project structuring
* Integration of frontend, backend, and ML logic

---

## 👩‍💻 Author

**Nandana Santhosh**
B.Tech Computer Science Engineering
LBS Institute of Technology for Women

---

## 📌 Note

This project was developed as an academic mini project to understand full-stack development, database systems, authentication, and clustering-based intelligent team formation.

This README will help you get started and resolve the `ORA-00942` error you encountered.
