from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from typing import List
from ..database.database import get_db  # Assumes you have a dependency that provides a Session
from ..models.models import Exercise
from ..schemas.exercise import ExerciseResponse

router = APIRouter(prefix="/exercises", tags=["exercises"])

@router.get("/lesson/{lesson_id}", response_model=List[ExerciseResponse])
def get_exercises_for_lesson(lesson_id: int, db: Session = Depends(get_db)):
    """
    Retrieve all exercises for a given lesson (topic) ordered by difficulty.
    """
    exercises = (
        db.query(Exercise)
          .order_by(Exercise.difficulty)
          .all()
    )
    if not exercises:
        raise HTTPException(status_code=404, detail="No exercises found for this lesson")
    return exercises
