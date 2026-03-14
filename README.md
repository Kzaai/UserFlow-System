🚀 UserFlow System v1.1
A professional, two-tier desktop management system built with Python and FastAPI. The project demonstrates a full data flow between a modern GUI and a RESTful backend, including role-based access and real-time monitoring.

🏗️ Architecture & Tech Stack
Backend: High-performance API built with FastAPI.

Data Validation: Strict modeling using Pydantic.

Database: Persistent storage using a flat-file JSON system (Scalable to SQL).

Frontend: Modern Desktop UI built with CustomTkinter.

Frame Switching: Dynamic UI state management for seamless transitions between Auth and Dashboard.

Asynchronous Tasks: Background monitoring and data fetching without UI freezing.

🌟 Key Features
Secure Authentication: Integrated login and registration flow with masked password inputs.

Dynamic Dashboard: Post-login user interface that adapts to the user's role.

Real-time API Heartbeat: A background "Status Dot" monitor that pings the server every 5 seconds using recursive .after() methods.

Role-Based Access (RBAC): Hidden Administrative Panel that unlocks only for users with specific credentials.

External API Integration (In Progress): Live weather data fetching using the OpenWeatherMap API to enhance the user dashboard.

1. Backend Setup

  cd backend
  pip install fastapi uvicorn pydantic
  uvicorn main:app --reload

2. Frontend Setup

  cd frontend
  pip install customtkinter requests
  python main.py


📈 Roadmap
[x] Basic Login/Registration Flow

[x] Heartbeat API Monitoring

[x] Admin Panel Implementation

[ ] Frame-based UI Refactoring (Current focus)

[ ] Live Weather Integration

[ ] SQL Database Migration (SQLite/PostgreSQL)


