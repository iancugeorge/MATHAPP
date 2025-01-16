import numpy as np
import sympy as sp
from typing import Dict, List, Tuple

def generate_exercise(exercise_type: str, difficulty: int) -> Dict:
    """
    Generates a math exercise based on type and difficulty.
    """
    if exercise_type == "arithmetic":
        return generate_arithmetic(difficulty)
    elif exercise_type == "equation":
        return generate_equation(difficulty)
    else:
        raise ValueError("Unsupported exercise type")

def generate_arithmetic(difficulty: int) -> Dict:
    """ Generates basic arithmetic problems """
    operators = ["+", "-", "*", "/"]
    num1 = np.random.randint(1, 10 * difficulty)
    num2 = np.random.randint(1, 10 * difficulty)
    op = np.random.choice(operators)
    
    if op == "/":
        num2 = np.random.randint(1, 10 * difficulty)  # Avoid division by zero
        num1 *= num2  # Ensure division is whole

    question = f"{num1} {op} {num2}"
    solution = eval(question)  # Safe for simple math operations

    hints = [f"Use {op} operation", f"Break numbers into smaller steps"]
    return {"type": "arithmetic", "difficulty": difficulty, "question": question, "solution": solution, "hints": hints}

def generate_equation(difficulty: int) -> Dict:
    """ Generates a simple algebraic equation """
    x = sp.Symbol('x')
    a = np.random.randint(1, 5 * difficulty)
    b = np.random.randint(1, 5 * difficulty)
    
    equation = sp.Eq(a * x + b, 0)
    solution = sp.solve(equation, x)

    hints = [f"Rearrange: {a}x = -{b}", "Divide by coefficient"]
    return {"type": "equation", "difficulty": difficulty, "question": str(equation), "solution": float(solution[0]), "hints": hints}
