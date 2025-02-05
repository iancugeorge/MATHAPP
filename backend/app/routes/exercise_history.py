from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from datetime import datetime
from typing import List
from ..database.database import get_db
from ..models.exercise_history import ExerciseHistory  # Ensure correct import path
from ..schemas.exercise_history import ExerciseHistoryResponse, ExerciseHistoryCreate  # Define these schemas similarly

router = APIRouter(prefix="/exercise-history", tags=["exercise-history"])

@router.post("/", response_model=ExerciseHistoryResponse)
def log_exercise_attempt(history_update: ExerciseHistoryCreate, db: Session = Depends(get_db)):
    """
    Log an exercise attempt.
    """
    history = ExerciseHistory(
        user_id=history_update.user_id,
        exercise_id=history_update.exercise_id,
        exercise_type=history_update.exercise_type,
        difficulty=history_update.difficulty,
        correct=history_update.correct,
        time_taken=history_update.time_taken,
        created_at=datetime.utcnow()
    )
    db.add(history)
    db.commit()
    db.refresh(history)
    return history

@router.get("/user/{user_id}", response_model=List[ExerciseHistoryResponse])
def get_exercise_history(user_id: int, db: Session = Depends(get_db)):
    """
    Get all exercise history entries for a specific user.
    """
    history_entries = db.query(ExerciseHistory).filter(ExerciseHistory.user_id == user_id).all()
    if not history_entries:
        raise HTTPException(status_code=404, detail="No exercise history found for this user")
    return history_entries
