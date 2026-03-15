# 🚀 UserFlow System v1.1

A professional, asynchronous desktop management system built with **Python** and **FastAPI**. This project demonstrates a complete data lifecycle: from a modern, stateful GUI to a RESTful backend with role-based access control.

## 🏗️ Architecture & Tech Stack

* **Backend:** High-performance REST API built with **FastAPI** & **Uvicorn**.
* **Data Integrity:** Strict schema validation using **Pydantic** models.
* **Database:** Persistent storage using a flat-file JSON system (Scalable to SQL).
* **Frontend:** Modern, hardware-accelerated UI using **CustomTkinter**.
* **State Management:** Dynamic UI transitions using a **Frame-based architecture** (`pack_forget` logic).
* **Asynchronous Operations:** Non-blocking background tasks for real-time API monitoring.

## 🌟 Key Features

* **Secure Authentication:** Full login/registration flow with real-time server-side validation.
* **Role-Based Access Control (RBAC):** Intelligent UI that dynamically injects the **Administrative Panel** only for authorized users.
* **Real-time API Heartbeat:** A recursive monitoring system (`.after()`) that tracks server availability with a visual status indicator.
* **Modular GUI Design:** Clean separation of concerns between Authentication, User Dashboard, and Admin tools.
* **Live Weather Integration (In Progress):** Integration with OpenWeatherMap API to provide contextual data.

## 🚀 Quick Start

### 1. Backend Setup
```bash
cd backend
pip install fastapi uvicorn pydantic
uvicorn main:app --reload

cd frontend
pip install customtkinter requests
python main.py



📈 Roadmap
[x] Basic Login/Registration Flow

[x] Heartbeat API Monitoring

[x] Frame-based UI Architecture (Stateful Views)

[x] Admin Panel Implementation (RBAC)

[ ] Live Weather Integration (Current Focus)

[ ] Start Screen Selection (Login vs Register)

[ ] SQL Database Migration (PostgreSQL)