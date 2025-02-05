from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from typing import List
from ..database.database import get_db  # Assumes you have a dependency that provides a Session
from ..models.models import Topic  # The SQLAlchemy model representing lessons (topics)
from ..schemas.topic import TopicResponse, TopicCreate

router = APIRouter(prefix="/lessons", tags=["lessons"])

@router.get("/", response_model=List[TopicResponse])
def get_lessons(db: Session = Depends(get_db)):
    """
    Retrieve a list of all lessons.
    """
    lessons = db.query(Topic).all()
    return lessons

@router.get("/{lesson_id}", response_model=TopicResponse)
def get_lesson(lesson_id: int, db: Session = Depends(get_db)):
    """
    Retrieve a specific lesson by its ID.
    """
    lesson = db.query(Topic).filter(Topic.id == lesson_id).first()
    if not lesson:
        raise HTTPException(status_code=404, detail="Lesson not found")
    return lesson

@router.post("/", response_model=TopicResponse, status_code=201)
def create_lesson(topic: TopicCreate, db: Session = Depends(get_db)):
    # Create a new Topic record from the TopicCreate schema
    new_topic = Topic(
        name=topic.name,
        description=topic.description,
        prerequisite_topics=topic.prerequisite_topics
    )
    db.add(new_topic)
    db.commit()
    db.refresh(new_topic)
    return new_topic