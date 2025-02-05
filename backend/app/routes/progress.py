from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from datetime import datetime
from typing import List
from ..database.database import get_db
from ..models.models import UserProgress, User  # Ensure your models are imported correctly
from ..schemas.progress import ProgressUpdate, ProgressResponse

router = APIRouter(prefix="/progress", tags=["progress"])

@router.get("/{user_id}", response_model=List[ProgressResponse])
def get_user_progress(user_id: int, db: Session = Depends(get_db)):
    """
    Retrieve progress data for a specific user.
    """
    progress_data = db.query(UserProgress).filter(UserProgress.user_id == user_id).all()
    if not progress_data:
        raise HTTPException(status_code=404, detail="Progress data not found for this user")
    return progress_data

@router.post("/{user_id}", response_model=ProgressResponse)
def update_user_progress(user_id: int, progress_update: ProgressUpdate, db: Session = Depends(get_db)):
    """
    Update the progress for a specific user and topic.
    If an entry for the user-topic combination exists, update it; otherwise, create a new record.
    """
    progress = db.query(UserProgress).filter(
        UserProgress.user_id == user_id,
        UserProgress.topic_id == progress_update.topic_id
    ).first()

    if progress:
        # Update the existing progress record:
        progress.exercises_completed += progress_update.exercises_completed
        progress.correct_exercises += progress_update.correct_exercises
        # Optionally adjust difficulty_level here based on your algorithm
        progress.last_activity = datetime.utcnow()
    else:
        # Create a new progress record if none exists:
        progress = UserProgress(
            user_id=user_id,
            topic_id=progress_update.topic_id,
            exercises_completed=progress_update.exercises_completed,
            correct_exercises=progress_update.correct_exercises,
            last_activity=datetime.utcnow()
        )
        db.add(progress)
    db.commit()
    db.refresh(progress)
    return progress
