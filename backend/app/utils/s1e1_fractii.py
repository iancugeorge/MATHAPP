import random
from fractions import Fraction
from typing import Dict, List, Union, Optional

class FractionArithmeticGenerator:
    def __init__(self):
        self.nice_fractions = [
            (1, 2), (1, 3), (1, 4), (2, 3), (3, 4), (1, 5),
            (2, 5), (3, 5), (4, 5), (1, 6), (5, 6), (1, 8),
            (3, 8), (5, 8), (7, 8), (1, 10), (3, 10), (7, 10)
        ]
        self.nice_results = [0, 1, 2, 3, 4, 5, 6, 7, 10]

    def get_nice_fraction(self, exclude: Optional[Fraction] = None) -> Fraction:
        """Returns a pedagogically nice fraction, optionally excluding a specific value."""
        while True:
            num, den = random.choice(self.nice_fractions)
            frac = Fraction(num, den)
            if exclude is None or frac != exclude:
                return frac

    def get_target_result(self) -> Union[int, Fraction]:
        """Returns a target result for the exercise."""
        if random.random() < 0.8:  # 80% chance for whole number
            return random.choice(self.nice_results)
        return self.get_nice_fraction()

    def format_number(self, num: Union[int, float, Fraction], style: str = 'fraction') -> str:
        """Formats numbers consistently."""
        if isinstance(num, (int, float)):
            num = Fraction(num).limit_denominator(100)
            
        if style == 'decimal':
            decimal = float(num)
            if decimal.is_integer():
                return str(int(decimal))
            return f"{decimal:.3f}".rstrip('0').rstrip('.')
            
        # Default to fraction format
        if num.denominator == 1:
            return str(num.numerator)
        return f"{num.numerator}/{num.denominator}"

    def generate_exercise(self, difficulty: int) -> Dict:
        """Generates fraction arithmetic exercises."""
        target = self.get_target_result()
        
        if difficulty == 1:
            # Simple fraction arithmetic
            frac1 = self.get_nice_fraction()
            frac2 = self.get_nice_fraction()
            multiplier = Fraction(target) / (frac1 + frac2)
            
            question = f"({self.format_number(frac1)} + {self.format_number(frac2)}) · {self.format_number(multiplier)}"
            steps = [
                f"Add fractions: {self.format_number(frac1)} + {self.format_number(frac2)}",
                f"Multiply result by {self.format_number(multiplier)}"
            ]
        
        else:  # difficulty == 2
            # More complex fraction arithmetic
            frac1 = self.get_nice_fraction()
            frac2 = self.get_nice_fraction()
            frac3 = self.get_nice_fraction()
            
            question = f"({self.format_number(frac1)} - {self.format_number(frac2)}) : {self.format_number(frac3)}"
            steps = [
                f"Subtract fractions: {self.format_number(frac1)} - {self.format_number(frac2)}",
                f"Divide result by {self.format_number(frac3)}"
            ]

        return {
            "type": "fraction_arithmetic",
            "difficulty": difficulty,
            "question": question,
            "solution": target,
            "latex": self.convert_to_latex(question),
            "hints": self.generate_hints(question, target, steps)
        }

    def convert_to_latex(self, expression: str) -> str:
        """Converts the expression to LaTeX format."""
        latex = expression
        latex = latex.replace(" · ", " \\cdot ")
        
        # Handle fractions
        while "/" in latex:
            idx = latex.find("/")
            # Find numerator
            num_end = idx
            num_start = idx - 1
            while num_start >= 0 and latex[num_start].isdigit():
                num_start -= 1
            num_start += 1
            
            # Find denominator
            den_start = idx + 1
            den_end = den_start
            while den_end < len(latex) and latex[den_end].isdigit():
                den_end += 1
                
            # Replace with LaTeX fraction
            numerator = latex[num_start:num_end]
            denominator = latex[den_start:den_end]
            replacement = f"\\frac{{{numerator}}}{{{denominator}}}"
            latex = latex[:num_start] + replacement + latex[den_end:]
        
        return f"${latex}$"

    def generate_hints(self, question: str, target: Union[int, Fraction], steps: List[str]) -> List[str]:
        """Generates appropriate hints for the exercise."""
        hints = [
            "Try converting all numbers to the same representation",
            "Look for common factors or patterns",
            f"The final answer should be {self.format_number(target)}"
        ]
        hints.extend(steps)
        return hints

# Example usage:
if __name__ == "__main__":
    generator = FractionArithmeticGenerator()
    for difficulty in [1, 2]:
        exercise = generator.generate_exercise(difficulty)
        print(f"\nDifficulty: {difficulty}")
        print(f"Question: {exercise['question']}")
        print(f"Solution: {exercise['solution']}")
        print(f"LaTeX: {exercise['latex']}")
        print("Hints:", exercise['hints'])