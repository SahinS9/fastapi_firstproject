from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.orm import relationship

from modelapi.database import Base

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String(20),nullable=False)
    email = Column(String(20), nullable=False, unique=True)
    task = relationship('Task', back_populates='owner', lazy=True)

    def __repr__(self):
        return f'user {self.id}: {self.name} with {self.email}'



class Task(Base):
    __tablename__ = 'tasks'
    id = Column(Integer, primary_key=True)
    name = Column(String(20),nullable=False)
    description = Column(String(100), nullable=True)
    deadline = Column(DateTime, nullable=True)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)

    owner = relationship('User', back_populates='task')

    def __repr__(self):
        return f'task {self.id}: {self.name} deadline: {self.deadline}'

    