import random
from dataclasses import dataclass
from typing import Dict, List, Union, Optional, Tuple
from dataclasses import field

@dataclass
class RadicalTerm:
    coefficient: int
    radicand: int
    
    def __post_init__(self):
        """Simplify the radical term after initialization"""
        if self.radicand < 0:
            raise ValueError("Negative radicands are not supported")

    def __str__(self) -> str:
        if self.coefficient == 0:
            return "0"
        if self.radicand == 1:
            return str(self.coefficient)
        if self.coefficient == 1:
            return f"√{self.radicand}"
        if self.coefficient == -1:
            return f"-√{self.radicand}"
        return f"{self.coefficient}√{self.radicand}"
    
    def __eq__(self, other) -> bool:
        if not isinstance(other, RadicalTerm):
            return NotImplemented
        return (self.coefficient == other.coefficient and 
                self.radicand == other.radicand)
    
    def multiply(self, other: 'RadicalTerm') -> 'RadicalTerm':
        """Multiply two RadicalTerms
        
        Examples: 
        - (2√3) × (4√5) = 8√15
        - √3 × √3 = 3  (because √3 × √3 = 3)
        - (2√3) × (2√3) = 12  (because 2√3 × 2√3 = 4 × 3 = 12)
        """
        new_coefficient = self.coefficient * other.coefficient
        
        # If multiplying same radicals, the radicands multiply and become coefficient
        if self.radicand == other.radicand:
            return RadicalTerm(new_coefficient * self.radicand, 1)
        
        # Otherwise multiply radicands normally
        new_radicand = self.radicand * other.radicand
        return RadicalTerm(new_coefficient, new_radicand)
    
    def can_combine(self, other: 'RadicalTerm') -> bool:
        return self.radicand == other.radicand
    
    def add(self, other: 'RadicalTerm') -> Optional['RadicalTerm']:
        if not self.can_combine(other):
            return None
        return RadicalTerm(
            coefficient=self.coefficient + other.coefficient,
            radicand=self.radicand
        )

@dataclass
class RadicalExpression:
    """Represents an expression that may include both rational and radical parts"""
    rational_part: int = 0  # For regular numbers
    radical_terms: List[RadicalTerm] = field(default_factory=list)
    
    def __str__(self) -> str:
        terms = []
        
        # Add rational part if non-zero
        if self.rational_part != 0:
            terms.append(str(self.rational_part))
        
        # Add non-zero radical terms
        terms.extend(str(term) for term in self.radical_terms if term.coefficient != 0)
        
        if not terms:
            return "0"
            
        return " + ".join(terms).replace(" + -", " - ")
    
    def simplify(self) -> 'RadicalExpression':
        """Combine like terms in the expression"""
        # Group like terms by radicand
        groups: Dict[int, List[RadicalTerm]] = {}
        for term in self.radical_terms:
            if term.radicand not in groups:
                groups[term.radicand] = []
            groups[term.radicand].append(term)
        
        # Combine terms in each group
        new_terms = []
        for radicand, terms in groups.items():
            total_coefficient = sum(term.coefficient for term in terms)
            if total_coefficient != 0:  # Only keep non-zero terms
                new_terms.append(RadicalTerm(total_coefficient, radicand))
        
        return RadicalExpression(self.rational_part, new_terms)

class RadicalExpressionGenerator:
    def __init__(self, seed: Optional[int] = None):
        """Initialize the generator with optional seed for reproducibility"""
        if seed is not None:
            random.seed(seed)
        self.nice_roots = [2, 3, 5, 7]
        self.nice_coefficients = [1, 2, 3]

    def generate_type1(self) -> Tuple[str, RadicalExpression, List[str]]:
        """
        Generates expression of form: √a(b + √a) - √a
        Returns: (question string, solution expression, step-by-step explanation)
        """
        root = random.choice(self.nice_roots)
        b = random.choice(self.nice_coefficients)
        
        # √a(b + √a) - √a = b√a + a - √a = b√a + (a-1)
        solution = RadicalExpression(
            rational_part=(root - 1),
            radical_terms=[RadicalTerm(b, root)]
        )
        
        question = f"√{root}({b} + √{root}) - √{root}"
        steps = [
            f"First distribute √{root}: (√{root} · {b}) + (√{root} · √{root}) - √{root}",
            f"Simplify √{root} · √{root} = {root}",
            f"Now we have: {b}√{root} + {root} - √{root}",
            f"Combine like terms with √{root}: {b}√{root} + ({root} - 1)",
            f"Final answer: {b}√{root} + {root - 1}"
        ]
        
        return question, solution, steps

    def generate_type2(self) -> Tuple[str, RadicalExpression, List[str]]:
        """
        Generates expression of form: (√a + b)(√a - b)
        Returns: (question string, solution expression, step-by-step explanation)
        """
        root = random.choice(self.nice_roots)
        b = random.choice(self.nice_coefficients)
        
        # (√a + b)(√a - b) = a - b²
        solution = RadicalExpression(rational_part=(root - b*b))
        
        question = f"(√{root} + {b})(√{root} - {b})"
        steps = [
            f"Use difference of squares formula: (a+b)(a-b) = a² - b²",
            f"Here, a = √{root} and b = {b}",
            f"Substitute: (√{root})² - ({b})²",
            f"Simplify (√{root})² = {root}",
            f"Calculate: {root} - {b}² = {root} - {b*b} = {root - b*b}"
        ]
        
        return question, solution, steps

    def generate_exercise(self, difficulty: int) -> Dict:
        """
        Generates radical expression exercises.
        Args:
            difficulty: 1 for type1 exercises, 2 for type2 exercises
        Returns:
            Dictionary containing exercise details
        Raises:
            ValueError: If difficulty is not 1 or 2
        """
        if difficulty not in [1, 2]:
            raise ValueError("Difficulty must be either 1 or 2")

        if difficulty == 1:
            question, solution, steps = self.generate_type1()
        else:
            question, solution, steps = self.generate_type2()

        return {
            "type": "radical_expression",
            "difficulty": difficulty,
            "question": question,
            "solution": str(solution),
            "latex": self.convert_to_latex(question),
            "hints": self.generate_hints(steps)
        }

    def convert_to_latex(self, expression: str) -> str:
        """
        Converts the expression to LaTeX format.
        Args:
            expression: The mathematical expression to convert
        Returns:
            LaTeX formatted string
        """
        latex = expression
        # Handle parentheses first
        latex = latex.replace("(", "\\left(").replace(")", "\\right)")
        
        # Replace square root symbol and add closing brace
        while "√" in latex:
            idx = latex.find("√")
            num_end = idx + 1
            while num_end < len(latex) and (latex[num_end].isdigit() or latex[num_end] == '.'):
                num_end += 1
            latex = latex[:idx] + "\\sqrt{" + latex[idx+1:num_end] + "}" + latex[num_end:]
        
        return f"${latex}$"

    def generate_hints(self, steps: List[str]) -> List[str]:
        """
        Generates appropriate hints for the exercise.
        Args:
            steps: List of solution steps
        Returns:
            List of hints including general tips and specific steps
        """
        hints = [
            "Remember the properties of square roots: √a · √a = a",
            "When multiplying terms with radicals, multiply the coefficients separately",
            "Look for opportunities to combine like radical terms"
        ]
        hints.extend(steps)
        return hints


def run_tests():
    """Run basic tests to verify the functionality"""
    generator = RadicalExpressionGenerator(seed=42)  # Set seed for reproducibility
    
    # Test RadicalTerm
    term1 = RadicalTerm(2, 3)
    term2 = RadicalTerm(2, 3)
    assert term1 == term2, "RadicalTerm equality failed"
    assert str(term1) == "2√3", "RadicalTerm string representation failed"
    
    # Test RadicalExpression
    expr1 = RadicalExpression(1, [RadicalTerm(2, 3)])
    expr2 = RadicalExpression(1, [RadicalTerm(2, 3)])
    assert expr1 == expr2, "RadicalExpression equality failed"
    assert str(expr1) == "1 + 2√3", "RadicalExpression string representation failed"
    
    # Test exercise generation
    exercise1 = generator.generate_exercise(1)
    exercise2 = generator.generate_exercise(2)
    assert all(key in exercise1 for key in ['question', 'solution', 'latex', 'hints']), "Missing keys in exercise1"
    assert all(key in exercise2 for key in ['question', 'solution', 'latex', 'hints']), "Missing keys in exercise2"
    
    print("All tests passed!")


if __name__ == "__main__":
    # Run tests first
    # Basic representation tests
    print("Basic tests:")
    print(RadicalTerm(2, 3))    # 2√3
    print(RadicalTerm(1, 5))    # √5
    print(RadicalTerm(-1, 2))   # -√2
    print(RadicalTerm(3, 1))    # 3
    print(RadicalTerm(0, 5))    # 0
    
    # Multiplication test
    print("\nMultiplication tests:")
    a = RadicalTerm(2, 3)  # 2√3
    b = RadicalTerm(4, 5)  # 4√5
    print(f"{a} × {b} = {a.multiply(b)}")  # Should be 8√15
    
    # Same radicand multiplication (should simplify)
    c = RadicalTerm(1, 3)  # √3
    d = RadicalTerm(1, 3)  # √3
    print(f"{c} × {d} = {c.multiply(d)}")  # Should be 3
    
    # Additional multiplication test with coefficients
    e = RadicalTerm(2, 3)  # 2√3
    f = RadicalTerm(2, 3)  # 2√3
    print(f"{e} × {f} = {e.multiply(f)}")  # Should be 12
    
    # Addition tests
    print("\nAddition tests:")
    g = RadicalTerm(2, 3)  # 2√3
    h = RadicalTerm(5, 3)  # 5√3
    i = RadicalTerm(2, 5)  # 2√5
    
    print(f"{g} + {h} = {g.add(h)}")  # Should be 7√3
    print(f"{g} + {i} = {g.add(i)}")  # Should be None
    
    # Test basic expressions
    print("Basic Expression Tests:")
    expr1 = RadicalExpression(3, [RadicalTerm(2, 5)])  # 3 + 2√5
    expr2 = RadicalExpression(0, [RadicalTerm(1, 3), RadicalTerm(1, 3)])  # √3 + √3
    expr3 = RadicalExpression(2, [RadicalTerm(1, 2), RadicalTerm(3, 2)])  # 2 + √2 + 3√2
    
    print(f"expr1: {expr1}")  # Should print: 3 + 2√5
    print(f"expr2: {expr2}")  # Should print: √3 + √3
    print(f"expr3: {expr3}")  # Should print: 2 + √2 + 3√2
    
    # Test simplification
    print("\nSimplification Tests:")
    print(f"expr2 simplified: {expr2.simplify()}")  # Should print: 2√3
    print(f"expr3 simplified: {expr3.simplify()}")  # Should print: 2 + 4√2
    
    # Generate and display example exercises
    generator = RadicalExpressionGenerator()
    for difficulty in [1, 2]:
        exercise = generator.generate_exercise(difficulty)
        print(f"\nDifficulty: {difficulty}")
        print(f"Question: {exercise['question']}")
        print(f"Solution: {exercise['solution']}")
        print(f"LaTeX: {exercise['latex']}")
        print("Hints:", exercise['hints'])