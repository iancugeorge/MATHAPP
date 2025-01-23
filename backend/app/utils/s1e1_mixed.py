import random
from fractions import Fraction
from decimal import Decimal, ROUND_HALF_UP
from typing import Dict, List, Union, Optional

class MixedRepresentationGenerator:
    def __init__(self):
        self.nice_fractions = [
            (1, 2), (1, 3), (1, 4), (2, 3), (3, 4), (1, 5),
            (2, 5), (3, 5), (4, 5), (1, 6), (5, 6), (1, 8),
            (3, 8), (5, 8), (7, 8), (1, 10), (3, 10), (7, 10)
        ]
        self.nice_results = [0, 1, 2, 3, 4, 5, 6, 7, 10]
        self.nice_whole_numbers = [2, 3, 4, 5, 6, 8, 10, 12, 15, 20, 30]
        self.nice_decimals = [0.25, 0.5, 0.75, 0.2, 0.4, 0.6, 0.8, 0.1, 0.3, 0.7, 0.9]

    def get_nice_fraction(self, exclude: Optional[Fraction] = None) -> Fraction:
        """Returns a pedagogically nice fraction, optionally excluding a specific value."""
        while True:
            num, den = random.choice(self.nice_fractions)
            frac = Fraction(num, den)
            if exclude is None or frac != exclude:
                return frac

    def get_nice_decimal(self, exclude: Optional[float] = None) -> float:
        """Returns a pedagogically nice decimal."""
        while True:
            decimal = random.choice(self.nice_decimals)
            if exclude is None or abs(decimal - exclude) > 0.01:
                return decimal

    def get_target_result(self) -> Union[int, float, Fraction]:
        """Returns a target result for the exercise."""
        choice = random.random()
        if choice < 0.4:  # 40% chance for whole number
            return random.choice(self.nice_results)
        elif choice < 0.7:  # 30% chance for decimal
            return self.get_nice_decimal()
        else:  # 30% chance for fraction
            return self.get_nice_fraction()

    def format_number(self, num: Union[int, float, Fraction], style: str = 'mixed') -> str:
        """Enhanced number formatting with multiple style options."""
        if isinstance(num, (int, float)):
            num = Fraction(num).limit_denominator(100)
            
        if style == 'decimal':
            decimal = float(num)
            if decimal.is_integer():
                return str(int(decimal))
            # Use Decimal for more precise rounding
            rounded = str(Decimal(str(decimal)).quantize(Decimal('0.001'), rounding=ROUND_HALF_UP))
            return rounded.rstrip('0').rstrip('.')
        
        if style == 'fraction':
            if num.denominator == 1:
                return str(num.numerator)
            return f"{num.numerator}/{num.denominator}"
        
        if style == 'mixed_number':
            if num.denominator == 1:
                return str(num.numerator)
            whole = num.numerator // num.denominator
            remain_num = num.numerator % num.denominator
            if whole == 0:
                return f"{remain_num}/{num.denominator}"
            return f"{whole} {remain_num}/{num.denominator}"
            
        # Default 'mixed' style - randomly choose representation
        if random.random() < 0.4:  # 40% chance for decimal
            return self.format_number(num, 'decimal')
        elif random.random() < 0.7:  # 30% chance for fraction
            return self.format_number(num, 'fraction')
        else:  # 30% chance for mixed number
            return self.format_number(num, 'mixed_number')

    def generate_exercise(self, difficulty: int) -> Dict:
        """Generates exercises mixing decimals and fractions."""
        target = self.get_target_result()
        
        if difficulty == 1:
            # Simple mixed representation
            operation = random.choice(['+', '-'])
            num1 = self.get_nice_fraction() if random.random() < 0.5 else self.get_nice_decimal()
            num2 = self.get_nice_decimal() if isinstance(num1, Fraction) else self.get_nice_fraction()
            
            question = f"{self.format_number(num1)} {operation} {self.format_number(num2)}"
            steps = [
                f"Convert both numbers to the same representation (either all decimals or all fractions)",
                f"Perform the {operation} operation",
                "Convert the result to simplest form"
            ]
        
        else:  # difficulty == 2
            # More complex mixed representation
            operation_type = random.choice(['multi_term', 'multiplication', 'division'])
            
            if operation_type == 'multi_term':
                # Three terms with mixed operations
                num1 = random.choice(self.nice_whole_numbers)
                num2 = self.get_nice_fraction()
                num3 = self.get_nice_decimal()
                operations = random.choice([('+', '-'), ('-', '+'), ('+', '·'), ('·', '+')])
                question = f"{num1} {operations[0]} {self.format_number(num2)} {operations[1]} {self.format_number(num3)}"
                steps = [
                    "Convert all numbers to the same representation",
                    f"Follow order of operations: multiplication/division before addition/subtraction",
                    "Combine terms and simplify"
                ]
            
            elif operation_type == 'multiplication':
                # Multiplication with parentheses
                num1 = self.get_nice_fraction()
                num2 = self.get_nice_decimal()
                num3 = random.choice(self.nice_whole_numbers)
                question = f"({self.format_number(num1)} + {num2}) · {num3}"
                steps = [
                    "First add the numbers in parentheses",
                    f"Convert result to suitable form for multiplication by {num3}",
                    "Multiply and simplify"
                ]
            
            else:  # division
                # Division with mixed representations
                num1 = self.get_nice_decimal()
                num2 = self.get_nice_fraction()
                question = f"{self.format_number(num1)} ÷ {self.format_number(num2)}"
                steps = [
                    f"Convert {self.format_number(num1)} and {self.format_number(num2)} to fractions",
                    "Recall: division by a fraction is the same as multiplication by its reciprocal",
                    "Multiply and simplify"
                ]

        return {
            "type": "mixed_representation",
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
        latex = latex.replace(" ÷ ", " \\div ")
        
        # Handle mixed numbers (e.g., "3 2/3" -> "3\frac{2}{3}")
        parts = latex.split()
        for i in range(len(parts)-1):
            if parts[i].isdigit() and "/" in parts[i+1]:
                num, den = parts[i+1].split("/")
                parts[i] = f"{parts[i]}\\frac{{{num}}}{{{den}}}"
                parts[i+1] = ""
        latex = " ".join(filter(None, parts))
        
        # Handle regular fractions
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

    def generate_hints(self, question: str, target: Union[int, Fraction, float], steps: List[str]) -> List[str]:
        """Generates appropriate hints for the exercise."""
        hints = [
            "Consider which representation (decimal or fraction) might be easier to work with",
            "Remember that decimals and fractions are different ways of representing the same values",
            f"The final answer should be {self.format_number(target)}",
            "Look for opportunities to simplify at each step"
        ]
        hints.extend(steps)
        return hints

# Example usage:
if __name__ == "__main__":
    generator = MixedRepresentationGenerator()
    for difficulty in [1, 2]:
        exercise = generator.generate_exercise(difficulty)
        print(f"\nDifficulty: {difficulty}")
        print(f"Question: {exercise['question']}")
        print(f"Solution: {exercise['solution']}")
        print(f"LaTeX: {exercise['latex']}")
        print("Hints:", exercise['hints'])