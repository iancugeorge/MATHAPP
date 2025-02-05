import random
import sympy as sp
from typing import Dict, Optional, List, Union

class exGenerator:
    def __init__(self, seed: Optional[int] = None):
        """Initialize the generator with optional seed for reproducibility"""
        self.random_state = random.Random(seed)
        self.nice_roots = [2, 3, 5, 7, 11, 13]
        self.nice_coefficients = list(range(1, 10))
        
    def convert_string_to_latex(self, raw_string: str) -> str:
        """
        Converts a human-formatted string into a LaTeX string without reordering.
        This function performs minimal substitution (e.g., replacing the radical symbol).
        """
        # Replace the Unicode square root with LaTeX \sqrt and wrap in math mode.
        latex_str = raw_string.replace("√", r"\sqrt")
        return f"{latex_str}"
    
    def _create_exercise_dict(self, question_str: str, expr, steps: List[str]) -> Dict:
        """
        Create a standardized exercise dictionary.
        For the question, we preserve the original string order (using our custom conversion).
        For the solution, we use the canonical output from sympy.
        """
        return {
            "type": "radical_expression",
            "difficulty": len(steps) - 2,
            "question": question_str,  # original human-readable string
            "questionLatex": self.convert_string_to_latex(question_str),
            "solution": str(expr),
            "solutionLatex": sp.latex(expr),
            "hints": self._generate_hints(steps)
        }
    
    def generate_type1(self) -> Dict:
        """
        Generates expression of form: √a(b + √a) - √a
        Returns: Dictionary with exercise details
        """
        root = random.choice(self.nice_roots)
        b = random.choice(self.nice_coefficients)

        # Build the expression symbolically for the solution.
        expr = sp.simplify(sp.sqrt(root) * (b + sp.sqrt(root)) - b * sp.sqrt(root))

        # Keep the original ordering as a formatted string.
        question_str = f"√{root}({b} + √{root}) - {b}√{root}"
                
        steps = [
            f"Mai întâi distribuim √{root}: (√{root} · {b}) + (√{root} · √{root}) - √{root}",
            f"Simplificăm √{root} · √{root} = {root}",
            f"Acum avem: {b}√{root} + {root} - √{root}",
            f"Combinăm termenii asemenea cu √{root}",
            f"Răspunsul final: {sp.latex(expr)}"
        ]
        
        return self._create_exercise_dict(question_str, expr, steps)    
    
    def generate_type2(self) -> Dict:
        """
        Generates expression of form: √a(√a + b) - √a
        Returns: Dictionary with exercise details
        """
        root = random.choice(self.nice_roots)
        b = random.choice(self.nice_coefficients)

        expr = sp.simplify(sp.sqrt(root) * (sp.sqrt(root) + b) - b * sp.sqrt(root))
        
        question_str = f"√{root}(√{root} + {b}) - {b}√{root}"
        steps = [
            f"Mai întâi distribuim √{root}: (√{root} · {b}) + (√{root} · √{root}) - √{root}",
            f"Simplificăm √{root} · √{root} = {root}",
            f"Acum avem: {b}√{root} + {root} - √{root}",
            f"Combinăm termenii asemenea cu √{root}",
            f"Răspunsul final: {str(expr)}"
        ]
        
        return self._create_exercise_dict(question_str, expr, steps)

    def generate_type3(self) -> Dict:
        """
        Generates expression of form: (√a + b)(√a - b)
        Returns: Dictionary with exercise details
        """
        root = random.choice(self.nice_roots)
        solution = '-1'
        while int(solution) < 0 or int(solution) > 81:
            b = random.choice(self.nice_coefficients)
            expr = sp.expand(sp.sqrt(root) + b) * (sp.sqrt(root) - b)
            simplified_expr = sp.simplify(expr)
            question_str = f"(√{root} + {b})(√{root} - {b})"
            solution = str(simplified_expr)        
            steps = [
                f"Folosim formula diferenței de pătrate: (a+b)(a-b) = a² - b²",
                f"Aici, a = √{root} și b = {b}",
                f"Înlocuim: (√{root})² - ({b})²",
                f"Simplificăm (√{root})² = {root}",
                f"Calculăm rezultatul final: {solution}"
            ]
        return self._create_exercise_dict(question_str, simplified_expr, steps)
        
    def generate_type4(self) -> Dict:
        """
        Generates expression of form: a(b + √c) - a√c
        Returns: Dictionary with exercise details
        """
        a = random.choice(self.nice_coefficients)
        b = random.choice(self.nice_coefficients)
        c = random.choice(self.nice_roots)
    
        expr = sp.simplify(a * (b + sp.sqrt(c)) - a * sp.sqrt(c))
        question_str = f"{a}({b} + √{c}) - {a}√{c}"
        steps = [
            f"Mai întâi distribuim {a}: ({a} · {b}) + ({a} · √{c}) - {a}√{c}",
            f"Acum avem: {a*b} + {a}√{c} - {a}√{c}",
            f"Combinăm termenii asemenea cu √{c}",
            f"Termenii cu √{c} se anulează",
            f"Răspunsul final: {str(expr)}"
        ]
            
        return self._create_exercise_dict(question_str, expr, steps)
    
    def generate_type5(self) -> Dict:
        """
        Generates expression of form: √a(b + c√a) - b√a + d
        Returns: Dictionary with exercise details
        """
        solution = '-1'
        while int(solution) < 0 or int(solution) > 81:
            a = random.choice(self.nice_roots)
            b = random.choice(self.nice_coefficients)
            c = random.choice(self.nice_coefficients)
            d = random.choice(self.nice_coefficients)
        
            expr = sp.simplify(sp.sqrt(a) * (b + c * sp.sqrt(a)) - b * sp.sqrt(a) + d)
            question_str = f"√{a}({b} + {c}√{a}) - {b}√{a} + {d}"
            solution = str(expr)
            steps = [
                f"Mai întâi distribuim √{a}: (√{a} · {b}) + (√{a} · {c}√{a}) - {b}√{a} + {d}",
                f"Simplificăm √{a} · √{a} = {a}",
                f"Acum avem: {b}√{a} + {c}{a} - {b}√{a} + {d}",
                f"Combinăm termenii asemenea cu √{a}",
                f"Termenii cu √{a} se anulează",
                f"Răspunsul final: {solution}"
            ]
        return self._create_exercise_dict(question_str, expr, steps)

    def generate_type6(self) -> Dict:
        """
        Generates expression of form: (a + √b)² - 2a√b
        Returns: Dictionary with exercise details
        """
        a = random.choice(self.nice_coefficients)
        b = random.choice(self.nice_roots)
                
        expr = sp.simplify((a + sp.sqrt(b))**2 - 2*a*sp.sqrt(b))
        question_str = f"({a} + √{b})² - {2*a}·√{b}"
        steps = [
            f"Mai întâi dezvoltăm ({a} + √{b})²",
            f"({a} + √{b})² = {a}² + 2·{a}·√{b} + (√{b})²",
            f"Simplificăm (√{b})² = {b}",
            f"Acum avem: {a*a} + 2·{a}·√{b} + {b} - 2·{a}·√{b}",
            f"Termenii 2·{a}·√{b} se anulează",
            f"Răspunsul final: {sp.latex(expr)}"
        ]
                
        return self._create_exercise_dict(question_str, expr, steps)

    def generate_type7(self) -> Dict:
        """
        Generates expression of form: √a(c - √c) + √c(√a - √(a*c))
        Returns: Dictionary with exercise details
        """
        a = random.choice(self.nice_roots)
        c = random.choice(self.nice_roots)
            
        expr = sp.simplify(sp.sqrt(a)*(c - sp.sqrt(c)) + sp.sqrt(c)*(sp.sqrt(a) - sp.sqrt(a*c)))
        question_str = f"√{a}({c} - √{c}) + √{c}(√{a} - √{a*c})"
        steps = [
            f"Mai întâi distribuim √{a} în primul termen: {c}√{a} - √{a}√{c}",
            f"Apoi distribuim √{c} în al doilea termen: √{c}√{a} - √{c}√{a*c}",
            f"Combinăm toți termenii: {c}√{a} - √{a}√{c} + √{c}√{a} - √{c}√{a*c}",
            f"Combinăm termenii asemenea cu √{a}√{c}",
            f"Simplificăm √{c}√{a*c} = √{c}·√{a*c} = √{a*c*c}",
            f"Răspunsul final: {str(expr)}"
        ]
            
        return self._create_exercise_dict(question_str, expr, steps)
            
    def generate_type8(self) -> Dict:
        """
        Generates expression of form: c*a*√b + c(d-a*√b)
        Returns: Dictionary with exercise details
        """
        solution = '-1'
        while int(solution) < 0 or int(solution) > 81:  
            a = random.choice(self.nice_coefficients)
            b = random.choice(self.nice_roots)
            c = random.choice(self.nice_coefficients)
            d = random.choice(self.nice_coefficients)
                    
            expr = sp.simplify(c*a*sp.sqrt(b) + c*(d - a*sp.sqrt(b)))
            question_str = f"{c*a}√{b} + {c}({d}-{a}√{b})"
            solution = str(expr)
            steps = [
                f"Mai întâi distribuim {c} în al doilea termen: {c}·{a}·√{b} + {c}·{d} - {c}·{a}·√{b}",
                f"Grupăm termenii asemenea cu {c}·{a}·√{b}",
                f"Termenii {c}·{a}·√{b} se anulează",
                f"Ne rămâne: {c}·{d}",
                f"Răspunsul final: {solution}"
            ]
        return self._create_exercise_dict(question_str, expr, steps)
    
    def generate_type9(self) -> Dict:
        """
        Generates expression of form: c*a·√b + c(d-√(b*a^2))
        Returns: Dictionary with exercise details
        """
        solution = '-1'
        while int(solution) < 0 or int(solution) > 81:
            a = random.choice(self.nice_coefficients)
            b = random.choice(self.nice_roots)
            c = random.choice(self.nice_coefficients)
            d = random.choice(self.nice_coefficients)
                    
            expr = sp.simplify(c*a*sp.sqrt(b) + c*(d - sp.sqrt(b*a**2)))
            question_str = f"{c*a}·√{b} + {c}({d}-√{b*a**2})"
            solution = str(expr)
            steps = [
                f"Mai întâi distribuim {c} în al doilea termen: {c}·{a}·√{b} + {c}·{d} - {c}·√{{b*a**2}}",
                f"Simplificăm √{{b*a**2}} = {a}·√{b}",
                f"Acum avem: {c}·{a}·√{b} + {c}·{d} - {c}·{a}·√{b}",
                f"Termenii {c}·{a}·√{b} se anulează",
                f"Ne rămâne: {c}·{d}",
                f"Răspunsul final: {solution}"
            ]
        return self._create_exercise_dict(question_str, expr, steps)
    
    def generate_type10(self) -> Dict:
        """
        Generates expression of form: √a(b+c√a) - b√a
        Returns: Dictionary with exercise details
        """
        solution = '-1'
        while int(solution) < 0 or int(solution) > 81:
            a = random.choice(self.nice_roots)
            b = random.choice(self.nice_coefficients)
            c = random.choice(self.nice_coefficients)
                    
            expr = sp.simplify(sp.sqrt(a)*(b + c*sp.sqrt(a)) - b*sp.sqrt(a))
            question_str = f"√{a}({b}+{c}√{a}) - {b}√{a}"
            solution = str(expr)
            steps = [
                f"Mai întâi distribuim √{a} în primul termen: {b}√{a} + {c}·{a} - {b}√{a}",
                f"Termenii {b}√{a} se anulează",
                f"Ne rămâne: {c}·{a}",
                f"Răspunsul final: {solution}"
            ]
        return self._create_exercise_dict(question_str, expr, steps)
    
    def generate_type11(self) -> Dict:
        """
        Generates expression of form: √a(c√a + b) - b√a
        Returns: Dictionary with exercise details
        """
        solution = '-1'
        while int(solution) < 0 or int(solution) > 81:  
            a = random.choice(self.nice_roots)
            b = random.choice(self.nice_coefficients)
            c = random.choice(self.nice_coefficients)
                    
            expr = sp.simplify(sp.sqrt(a)*(c*sp.sqrt(a) + b) - b*sp.sqrt(a))
            question_str = f"√{a}({c}√{a} + {b}) - {b}√{a}"
            solution = str(expr)
            steps = [
                f"Mai întâi distribuim √{a} în primul termen: {c}·{a} + {b}√{a} - {b}√{a}",
                f"Termenii {b}√{a} se anulează",
                f"Ne rămâne: {c}·{a}",
                f"Răspunsul final: {solution}"
            ]
        return self._create_exercise_dict(question_str, expr, steps)
    
    def generate_type12(self) -> Dict:
        """
        Generates expression of form: (√(a²b) + c)(a√b - c)
        Returns: Dictionary with exercise details
        """
        solution = '-1'
        while int(solution) < 0 or int(solution) > 81:
            a = random.choice(self.nice_coefficients)
            b = random.choice(self.nice_roots)
            c = random.choice(self.nice_coefficients)
                    
            sqrt_a2b = sp.sqrt(a**2 * b)
            expr = sp.expand((sqrt_a2b + c)*(a*sp.sqrt(b) - c))
            question_str = f"(√{(a**2)*b} + {c})({a}√{b} - {c})"
            solution = str(expr)
            steps = [
                f"Mai întâi simplificăm √({a}²·{b}) = {a}√{b}",
                f"Acum avem ({a}√{b} + {c})({a}√{b} - {c})",
                f"Aceasta este formula diferenței de pătrate: (p + q)(p - q) = p² - q²",
                f"Aici p = {a}√{b} și q = {c}",
                f"Deci obținem ({a}√{b})² - ({c})²",
                f"Simplificăm: {a}²·{b} - {c}²",
                f"Răspunsul final: {solution}"
            ]
        return self._create_exercise_dict(question_str, expr, steps)
    
    def generate_type13(self) -> Dict:
        """
        Generates expression of form: (a + √b)² + (1 - a√b)²
        Returns: Dictionary with exercise details
        """
        solution = '-1'
        while int(solution) < 0 or int(solution) > 81:
            a = random.choice(self.nice_coefficients)
            b = random.choice(self.nice_roots)
                    
            sqrt_b = sp.sqrt(b)
            expr1 = (a + sqrt_b)**2
            expr2 = (1 - a*sqrt_b)**2
            expr = sp.expand(expr1 + expr2)
            question_str = f"({a} + √{b})² + (1 - {a}√{b})²"
            solution = str(expr)
            steps = [
                f"Să rezolvăm pas cu pas folosind formula pătratului unui binom: (x + y)² = x² + 2xy + y²",
                f"Prima parte ({a} + √{b})²: {a}² + 2·{a}·√{b} + (√{b})²",
                f"Simplificăm prima parte: {a**2} + {2*a}√{b} + {b}",
                f"A doua parte (1 - {a}√{b})²: 1² + 2·1·(-{a}√{b}) + ({-a}√{b})²", 
                f"Simplificăm a doua parte: 1 - {2*a}√{b} + {a**2}·{b}",
                f"Adunăm ambele părți și combinăm termenii asemenea",
                f"Răspunsul final: {solution}"
            ]
        return self._create_exercise_dict(question_str, expr, steps)
    
    def generate_exercise(self, difficulty: int) -> Dict:
        """Generates radical expression exercises."""
        try:
            generator_method = getattr(self, f'generate_type{difficulty}')
            return generator_method()
        except AttributeError:
            raise ValueError(f"Invalid exercise type: {difficulty}")

    def _convert_to_latex(self, expr: Union[sp.Expr, str]) -> str:
        """
        Converts the expression to LaTeX format using Sympy.
        Handles both Sympy expressions and string inputs.
        (This method is kept for potential future use, but for question display we use our custom converter.)
        """
        if isinstance(expr, str):
            return expr
        return sp.latex(expr)
    
    def _generate_hints(self, steps: List[str]) -> List[str]:
        """
        Generates comprehensive hints for the exercise.
        Provides general mathematical tips and specific solution steps.
        """
        general_hints = [
            # You can add general hints here if needed.
        ]
        return general_hints + steps  # Limit specific steps to avoid overwhelming hints

Generator = exGenerator