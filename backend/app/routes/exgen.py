# from fastapi import APIRouter, Query
# from typing import Dict
# from ..utils.exgen import generate_exercise
# from ..utils.s1e1_radicali import RadicalExpressionGenerator

# router = APIRouter(prefix="/exercises", tags=["exercises"])

# @router.get("/s1e1", response_model=Dict)
# def get_exercise(exercise_type: str = Query("radical"), difficulty: int = Query(None)):
#     """
#     API route to generate exercises dynamically.
#     """
#     try:
#         generator = RadicalExpressionGenerator()
#         if difficulty is None:
#             import random
#             difficulty = random.randint(1, 14)
#         exercise = generator.generate_exercise(difficulty)
#         return exercise
#     except ValueError as e:
#         return {"error": str(e)}
# routes/exgen.py

from fastapi import HTTPException
import importlib.util
import os

def get_generator_for_lesson(lesson_code: str):
    """
    Dynamically loads a generator module from the utils folder using the lesson_code.
    For example, if lesson_code is "001", this will attempt to load the module from "utils/001.py".
    The module must define a class named 'Generator'.
    """
    # Construct the file path
    module_path = os.path.join(os.path.dirname(__file__), "..", "utils", f"{lesson_code}.py")
    
    if not os.path.exists(module_path):
        raise HTTPException(status_code=400, detail=f"Module file not found for lesson code '{lesson_code}'.")

    spec = importlib.util.spec_from_file_location(f"module_{lesson_code}", module_path)
    if spec is None or spec.loader is None:
        raise HTTPException(status_code=400, detail=f"Could not load module for lesson code '{lesson_code}'.")
    
    module = importlib.util.module_from_spec(spec)
    try:
        spec.loader.exec_module(module)
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Error executing module for lesson code '{lesson_code}': {e}")
    
    # Retrieve the Generator class from the module
    generator_class = getattr(module, "Generator", None)
    if generator_class is None:
        raise HTTPException(status_code=400, detail=f"Module for lesson code '{lesson_code}' does not export 'Generator'.")
    
    return generator_class

from fastapi import APIRouter, Query, HTTPException
from typing import Dict
import random

router = APIRouter(prefix="/exercises", tags=["exercises"])

@router.get("/{lesson_code}", response_model=Dict)
def get_exercise(lesson_code: str, difficulty: int = Query(None)):
    """
    API route to generate an exercise for a specific lesson.
    The lesson_code is used directly to load the module from the utils folder.
    For example, lesson_code "001" will load "utils/001.py".
    """
    # Load the generator class dynamically from the file corresponding to the lesson code
    GeneratorClass = get_generator_for_lesson(lesson_code)
    generator = GeneratorClass()
    
    if difficulty is None:
        difficulty = random.randint(1, 14)
    
    try:
        exercise = generator.generate_exercise(difficulty)
        return exercise
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error generating exercise: {e}")
