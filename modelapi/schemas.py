from pydantic import BaseModel


### USER ###
class UserBase(BaseModel):
    name: str

class User(UserBase):
    id: int
    name: str
    email: str

class UserCreate(UserBase):
    email: str



### TASK ###
class TaskBase(BaseModel):
    name: str
    description: str | None=None

class TaskCreate(TaskBase):
    pass

class Task(TaskBase):
    id: int
    name: str
    description: str
    user_id: int

    class Config:
        orm_mode=True
