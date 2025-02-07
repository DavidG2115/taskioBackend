from pydantic import BaseModel

class TaskBase(BaseModel):
    title: str
    description: str = None
    completed: bool = False
    icon : str = None

class TaskCreate(TaskBase):
    pass

class TaskResponse(TaskBase):
    id: int

    class Config:
        orm_mode = True

# Esquema para crear un usuario
class UserCreate(BaseModel):
    username: str
    email: str

# Esquema para responder con datos de usuario
class UserResponse(BaseModel):
    id: int
    username: str
    email: str

    class Config:
        orm_mode = True  # Para convertir SQLAlchemy en JSON