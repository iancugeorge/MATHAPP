from fastapi import APIRouter, Query
from typing import Dict
from ..utils.exgen import generate_exercise

router = APIRouter(prefix="/exercises", tags=["exercises"])

@router.get("/generate", response_model=Dict)
def get_exercise(exercise_type: str = Query("arithmetic"), difficulty: int = Query(1)):
    """
    API route to generate exercises dynamically.
    """
    try:
        exercise = generate_exercise(exercise_type, difficulty)
        return exercise
    except ValueError as e:
        return {"error": str(e)}
