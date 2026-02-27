from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from .database import Base, engine, SessionLocal
from . import models, schemas, security, auth, detections

Base.metadata.create_all(bind=engine)

app = FastAPI(title="SecureLog Sentinel")

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/register")
def register(user: schemas.UserCreate, db: Session = Depends(get_db)):
    hashed = security.hash_password(user.password)
    db_user = models.User(username=user.username, hashed_password=hashed, role=user.role)
    db.add(db_user)
    db.commit()
    return {"message": "User created"}

@app.post("/login")
def login(user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = db.query(models.User).filter(models.User.username == user.username).first()
    if not db_user or not security.verify_password(user.password, db_user.hashed_password):
        raise HTTPException(status_code=400, detail="Invalid credentials")
    token = security.create_access_token({"sub": db_user.username})
    return {"access_token": token}

@app.post("/logs")
def ingest_log(log: schemas.LogCreate, db: Session = Depends(get_db), user=Depends(auth.get_current_user)):
    entry = models.LogEntry(**log.dict())
    db.add(entry)
    db.commit()
    return {"message": "Log stored"}

@app.get("/detect")
def run_detection(db: Session = Depends(get_db), user=Depends(auth.require_admin)):
    logs = db.query(models.LogEntry).all()
    alerts = detections.detect_bruteforce(logs)
    return {"alerts": alerts}
