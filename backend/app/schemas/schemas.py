from pydantic import BaseModel, EmailStr
from typing import List, Optional
from datetime import datetime

class UserBase(BaseModel):
    username: str
    email: EmailStr

class UserCreate(UserBase):
    password: str

class UserResponse(UserBase):
    id: int
    created_at: datetime
    progress_level: int
    is_active: bool

    class Config:
        from_attributes = True

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    username: Optional[str] = None

class ExerciseBase(BaseModel):
    type: str
    difficulty: int
    question: str
    solution: float
    hints: List[str]

class ExerciseCreate(ExerciseBase):
    pass

class ExerciseResponse(ExerciseBase):
    id: str
    steps: List[str]

    class Config:
        from_attributes = True

class ProgressUpdate(BaseModel):
    topic_id: int
    exercises_completed: int
    correct_exercises: int

class ProgressResponse(BaseModel):
    user_id: int
    topic_id: int
    difficulty_level: int
    exercises_completed: int
    correct_exercises: int
    last_activity: datetime

    class Config:
        from_attributes = True