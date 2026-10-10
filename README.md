# FastAPI Quality Scanner Demo

A sample FastAPI application demo with PostgreSQL, SQLAlchemy, and Docker.

## Setup & Run Instructions

### 1. Start Database with Docker Compose
```bash
docker compose up -d
```

### 2. Install Python Dependencies
```bash
pip install -r requirements.txt
```

### 3. Run FastAPI Application
```bash
uvicorn app.main:app --reload
```

### 4. Access API Documentation
Open your browser at:
http://localhost:8000/docs
