from pydantic import BaseModel
from typing import List

class ExerciseBase(BaseModel):
    type: str
    difficulty: int
    question: str
    solution: float
    hints: List[str]

class ExerciseCreate(ExerciseBase):
    pass

class ExerciseResponse(ExerciseBase):
    id: int
    # Optionally include steps if needed; for now, we can leave that out or add later.
    steps: List[str] = []  # Default to empty list if not provided

    class Config:
        from_attributes = True