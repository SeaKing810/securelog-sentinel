# SecureLog Sentinel

SecureLog Sentinel is a containerized log ingestion and detection API built with FastAPI.

Features
- JWT Authentication
- Role Based Access Control
- Secure Password Hashing
- Brute Force Detection Logic
- SQLite Persistence
- Dockerized Deployment
- Unit Testing

Tech Stack
- Python
- FastAPI
- SQLAlchemy
- JWT
- Docker

Run locally

pip install -r requirements.txt
uvicorn app.main:app --reload

Or use Docker

docker-compose up --build

Why this project exists

This project demonstrates secure backend engineering principles,
including authentication, authorization, structured logging,
and detection engineering.

This is a defensive security project for portfolio purposes.
