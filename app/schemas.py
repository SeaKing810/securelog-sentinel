from pydantic import BaseModel

class UserCreate(BaseModel):
    username: str
    password: str
    role: str = "analyst"

class LogCreate(BaseModel):
    message: str
    source_ip: str
    severity: str = "info"
