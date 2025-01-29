from fastapi import APIRouter, Query
from typing import Dict
from ..utils.exgen import generate_exercise
from ..utils.s1e1_radicali import RadicalExpressionGenerator

router = APIRouter(prefix="/exercises", tags=["exercises"])

@router.get("/s1e1", response_model=Dict)
def get_exercise(exercise_type: str = Query("radical"), difficulty: int = Query(None)):
    """
    API route to generate exercises dynamically.
    """
    try:
        generator = RadicalExpressionGenerator()
        if difficulty is None:
            import random
            difficulty = random.randint(1, 12)
        exercise = generator.generate_exercise(difficulty)
        return exercise
    except ValueError as e:
        return {"error": str(e)}