import random
import sympy as sp
from typing import Dict, Optional, List

class RadicalExpressionGenerator:
    def __init__(self, seed: Optional[int] = None):
        """Initialize the generator with optional seed for reproducibility"""
        if seed is not None:
            random.seed(seed)
        self.nice_roots = [2, 3, 5, 7, 11, 13]
        self.nice_coefficients = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    def generate_type1(self) -> Dict:
        """
        Generates expression of form: √a(b + √a) - √a
        Returns: Dictionary with exercise details
        """
        root = random.choice(self.nice_roots)
        b = random.choice(self.nice_coefficients)

        # Construct the expression symbolically
        expr = sp.simplify(sp.sqrt(root) * (b + sp.sqrt(root)) - b * sp.sqrt(root))
        
        question = f"√{root}({b} + √{root}) - {b}√{root}"
        solution = str(expr)
        
        steps = [
            f"First distribute √{root}: (√{root} · {b}) + (√{root} · √{root}) - √{root}",
            f"Simplify √{root} · √{root} = {root}",
            f"Now we have: {b}√{root} + {root} - √{root}",
            f"Combine like terms with √{root}",
            f"Final answer: {solution}"
        ]
        
        return {
            "type": "radical_expression",
            "difficulty": 1,
            "question": question,
            "questionLatex": self._convert_to_latex(question),
            "solution": solution,
            "solutionLatex": self._convert_to_latex(expr),
            "hints": self._generate_hints(steps)
        }
    
    def generate_type2(self) -> Dict:
        """
        Generates expression of form: √a(√a + b) - √a
        Returns: Dictionary with exercise details
        """
        root = random.choice(self.nice_roots)
        b = random.choice(self.nice_coefficients)

        # Construct the expression symbolically
        expr = sp.simplify(sp.sqrt(root) * (sp.sqrt(root) + b) - b * sp.sqrt(root))
        
        question = f"√{root}(√{root} + {b}) - {b}√{root}"
        solution = str(expr)
        
        steps = [
            f"First distribute √{root}: (√{root} · {b}) + (√{root} · √{root}) - √{root}",
            f"Simplify √{root} · √{root} = {root}",
            f"Now we have: {b}√{root} + {root} - √{root}",
            f"Combine like terms with √{root}",
            f"Final answer: {solution}"
        ]
        
        return {
            "type": "radical_expression",
            "difficulty": 1,
            "question": question,
            "questionLatex": self._convert_to_latex(question),
            "solution": solution,
            "solutionLatex": self._convert_to_latex(expr),
            "hints": self._generate_hints(steps)
        }

    def generate_type3(self) -> Dict:
        """
        Generates expression of form: (√a + b)(√a - b)
        Returns: Dictionary with exercise details
        """
        root = random.choice(self.nice_roots)
        # Ensure root is large enough compared to b
        while True:
            b = random.choice(self.nice_coefficients)
            if root >= b * b:
                break
        
        # Construct the expression symbolically
        # Use fully simplified version
        expr = sp.expand(sp.sqrt(root) + b) * (sp.sqrt(root) - b)
        simplified_expr = sp.simplify(expr)
        
        question = f"(√{root} + {b})(√{root} - {b})"
        solution = str(simplified_expr)        
        steps = [
            f"Use difference of squares formula: (a+b)(a-b) = a² - b²",
            f"Here, a = √{root} and b = {b}",
            f"Substitute: (√{root})² - ({b})²",
            f"Simplify (√{root})² = {root}",
            f"Calculate final result: {solution}"
        ]
        
        return {
            "type": "radical_expression",
            "difficulty": 2,
            "question": question,
            "solution": solution,
            "latex": self._convert_to_latex(simplified_expr),
            "hints": self._generate_hints(steps)
        }
        
    def generate_type4(self) -> Dict:
            """
            Generates expression of form: a(b + √c) - a√c
            Returns: Dictionary with exercise details
            """
            a = random.choice(self.nice_coefficients)
            b = random.choice(self.nice_coefficients)
            c = random.choice(self.nice_roots)
    
            # Construct the expression symbolically
            expr = sp.simplify(a * (b + sp.sqrt(c)) - a * sp.sqrt(c))
            
            question = f"{a}({b} + √{c}) - {a}√{c}"
            solution = str(expr)
            
            steps = [
                f"First distribute {a}: ({a} · {b}) + ({a} · √{c}) - {a}√{c}",
                f"Now we have: {a*b} + {a}√{c} - {a}√{c}",
                f"Combine like terms with √{c}",
                f"The √{c} terms cancel out",
                f"Final answer: {solution}"
            ]
            
            return {
                "type": "radical_expression",
                "difficulty": 1,
                "question": question,
                "questionLatex": self._convert_to_latex(question),
                "solution": solution,
                "solutionLatex": self._convert_to_latex(expr),
                "hints": self._generate_hints(steps)
            }
    
    def generate_type5(self) -> Dict:
            """
            Generates expression of form: √a(b + c√a) - b√a + d
            Returns: Dictionary with exercise details
            """
            a = random.choice(self.nice_roots)
            b = random.choice(self.nice_coefficients)
            c = random.choice(self.nice_coefficients)
            d = random.choice(self.nice_coefficients)
    
            # Construct the expression symbolically
            expr = sp.simplify(sp.sqrt(a) * (b + c * sp.sqrt(a)) - b * sp.sqrt(a) + d)
            
            question = f"√{a}({b} + {c}√{a}) - {b}√{a} + {d}"
            solution = str(expr)
            
            steps = [
                f"First distribute √{a}: (√{a} · {b}) + (√{a} · {c}√{a}) - {b}√{a} + {d}",
                f"Simplify √{a} · √{a} = {a}",
                f"Now we have: {b}√{a} + {c}{a} - {b}√{a} + {d}",
                f"Combine like terms with √{a}",
                f"The √{a} terms cancel out",
                f"Final answer: {solution}"
            ]
            
            return {
                "type": "radical_expression",
                "difficulty": 2,
                "question": question,
                "questionLatex": self._convert_to_latex(question),
                "solution": solution,
                "solutionLatex": self._convert_to_latex(expr),
                "hints": self._generate_hints(steps)
            }
    def generate_type6(self) -> Dict:
                """
                Generates expression of form: (a + √b)² - 2a√b
                Returns: Dictionary with exercise details
                """
                a = random.choice(self.nice_coefficients)
                b = random.choice(self.nice_roots)
                
                # Construct the expression symbolically
                expr = sp.simplify((a + sp.sqrt(b))**2 - 2*a*sp.sqrt(b))
                
                question = f"({a} + √{b})² - {2*a}·√{b}"
                solution = str(expr)
                
                steps = [
                    f"First expand ({a} + √{b})²",
                    f"({a} + √{b})² = {a}² + 2·{a}·√{b} + (√{b})²",
                    f"Simplify (√{b})² = {b}",
                    f"Now we have: {a*a} + 2·{a}·√{b} + {b} - 2·{a}·√{b}",
                    f"The 2·{a}·√{b} terms cancel out",
                    f"Final answer: {solution}"
                ]
                
                return {
                    "type": "radical_expression",
                    "difficulty": 2,
                    "question": question,
                    "questionLatex": self._convert_to_latex(question),
                    "solution": solution,
                    "solutionLatex": self._convert_to_latex(expr),
                    "hints": self._generate_hints(steps)
                }
    def generate_type7(self) -> Dict:
            """
            Generates expression of form: √a(c - √c) + √c(√a - √(a*c))
            Returns: Dictionary with exercise details
            """
            a = random.choice(self.nice_roots)
            c = random.choice(self.nice_roots)
            
            # Construct the expression symbolically
            expr = sp.simplify(sp.sqrt(a)*(c - sp.sqrt(c)) + sp.sqrt(c)*(sp.sqrt(a) - sp.sqrt(a*c)))
            
            question = f"√{a}({c} - √{c}) + √{c}(√{a} - √{a*c})"
            solution = str(expr)
            
            steps = [
                f"First distribute √{a} in the first term: {c}√{a} - √{a}√{c}",
                f"Then distribute √{c} in the second term: √{c}√{a} - √{c}√{a*c}",
                f"Combine all terms: {c}√{a} - √{a}√{c} + √{c}√{a} - √{c}√{a*c}",
                f"Combine like terms with √{a}√{c}",
                f"Simplify √{c}√{a*c} = √{c}·√{a*c} = √{a*c*c}",
                f"Final answer: {solution}"
            ]
            
            return {
                "type": "radical_expression",
                "difficulty": 2,
                "question": question,
                "questionLatex": self._convert_to_latex(question),
                "solution": solution,
                "solutionLatex": self._convert_to_latex(expr),
                "hints": self._generate_hints(steps)
            }
    

    def generate_exercise(self, difficulty: int) -> Dict:
        """
        Generates radical expression exercises.
        Args:
            difficulty: Integer representing the exercise type
        Returns:
            Dictionary containing exercise details
        Raises:
            ValueError: If difficulty is not a valid type
        """
        if hasattr(self, f'generate_type{difficulty}'):
            return getattr(self, f'generate_type{difficulty}')()
        else:
            raise ValueError(f"Invalid exercise type: {difficulty}")

    def _convert_to_latex(self, expr) -> str:
        """
        Converts the expression to LaTeX format using SymPy.
        Args:
            expr: SymPy symbolic expression
        Returns:
            LaTeX formatted string
        """
        return f"${sp.latex(expr)}$"

    def _generate_hints(self, steps: List[str]) -> List[str]:
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
            "Look for opportunities to simplify radical expressions"
        ]
        hints.extend(steps)
        return hints

if __name__ == "__main__":
    # Run tests first
    generator = RadicalExpressionGenerator()
    
    # Generate type 1 exercise
    exercise1 = generator.generate_exercise(1)
    print("Type 1 Exercise:")
    print("Question:", exercise1['question'])
    print("Solution:", exercise1['solution'])
    print("LaTeX:", exercise1['latex'])
    print("Hints:", exercise1['hints'])
    
    # Generate type 2 exercise
    exercise2 = generator.generate_exercise(2)
    print("\nType 2 Exercise:")
    print("Question:", exercise2['question'])
    print("Solution:", exercise2['solution'])
    print("LaTeX:", exercise2['latex'])
    print("Hints:", exercise2['hints'])