# 🚀 UserFlow System v1.0

A modern, two-tier system for user registration and management.

Update: Basic registration flow is functional. Data is sent via POST requests and stored in a local JSON database.

### 🏗️ Architecture:
* **Backend (`/backend`):** High-performance API built with **FastAPI**.
* **Frontend (`/frontend`):** Desktop application built with **CustomTkinter**.

### 🛠️ Backend Technical Details:
* **Data Modeling:** Used `Pydantic` (BaseModel) for strict data validation. 
* **POST Method:** Secure user registration via hidden payload (Request Body). 
* **Storage:** Persistent flat-file database using **JSON**.


### 📖 How to test the Server:
1. `cd backend`
2. `uvicorn main:app --reload`
3. Visit `http://127.0.0` to use the interactive Swagger UI. 
