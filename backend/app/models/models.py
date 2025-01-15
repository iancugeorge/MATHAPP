from sqlalchemy import Boolean, Column, Integer, String, ForeignKey, TIMESTAMP, ARRAY, Float
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from ..database.database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(50), unique=True, nullable=False)
    email = Column(String(100), unique=True, nullable=False)
    password_hash = Column(String(100), nullable=False)
    created_at = Column(TIMESTAMP(timezone=True), server_default=func.now())
    progress_level = Column(Integer, default=1)
    is_active = Column(Boolean, default=True)

    # Relationships
    progress = relationship("UserProgress", back_populates="user")
    exercise_history = relationship("ExerciseHistory", back_populates="user")

class Topic(Base):
    __tablename__ = "topics"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(50))
    description = Column(String)
    prerequisite_topics = Column(ARRAY(Integer))

class UserProgress(Base):
    __tablename__ = "user_progress"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    topic_id = Column(Integer, ForeignKey("topics.id"))
    difficulty_level = Column(Integer, default=1)
    exercises_completed = Column(Integer, default=0)
    correct_exercises = Column(Integer, default=0)
    last_activity = Column(TIMESTAMP(timezone=True), server_default=func.now())

    # Relationships
    user = relationship("User", back_populates="progress")
    topic = relationship("Topic")

class ExerciseHistory(Base):
    __tablename__ = "exercise_history"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    exercise_id = Column(String(50))
    exercise_type = Column(String(20))
    difficulty = Column(Integer)
    correct = Column(Boolean)
    time_taken = Column(Float)
    created_at = Column(TIMESTAMP(timezone=True), server_default=func.now())

    # Relationships
    user = relationship("User", back_populates="exercise_history")