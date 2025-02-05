from pydantic import BaseModel
from datetime import datetime
from typing import Optional

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