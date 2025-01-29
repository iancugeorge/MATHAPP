import random
import sympy as sp
from typing import Dict, Optional, List, Union

class RadicalExpressionGenerator:
    def __init__(self, seed: Optional[int] = None):
        """Initialize the generator with optional seed for reproducibility"""
        self.random_state = random.Random(seed)
        self.nice_roots = [2, 3, 5, 7, 11, 13]
        self.nice_coefficients = list(range(1, 10))
        
    def _create_exercise_dict(self, question: str, expr, steps: List[str]) -> Dict:
        """Create a standardized exercise dictionary."""
        return {
            "type": "radical_expression",
            "difficulty": len(steps) - 2,  # Rough difficulty estimation
            "question": question,
            "questionLatex": self._convert_to_latex(question),
            "solution": str(expr),
            "solutionLatex": self._convert_to_latex(expr),
            "hints": self._generate_hints(steps)
        }
    
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
            f"Mai întâi distribuim √{root}: (√{root} · {b}) + (√{root} · √{root}) - √{root}",
            f"Simplificăm √{root} · √{root} = {root}",
            f"Acum avem: {b}√{root} + {root} - √{root}",
            f"Combinăm termenii asemenea cu √{root}",
            f"Răspunsul final: {solution}"
        ]
        
        return self._create_exercise_dict(question, expr, steps)
    
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
            f"Mai întâi distribuim √{root}: (√{root} · {b}) + (√{root} · √{root}) - √{root}",
            f"Simplificăm √{root} · √{root} = {root}",
            f"Acum avem: {b}√{root} + {root} - √{root}",
            f"Combinăm termenii asemenea cu √{root}",
            f"Răspunsul final: {solution}"
        ]
        
        return self._create_exercise_dict(question, expr, steps)

    def generate_type3(self) -> Dict:
        """
        Generates expression of form: (√a + b)(√a - b)
        Returns: Dictionary with exercise details
        """
        root = random.choice(self.nice_roots)
        # # Ensure root is large enough compared to b
        # while True:
        #     b = random.choice(self.nice_coefficients)
        #     if root >= b * b:
        #         break
        solution = '-1'
        while int(solution) < 0 or int(solution) > 81:
            b = random.choice(self.nice_coefficients)
            # Construct the expression symbolically
            # Use fully simplified version
            expr = sp.expand(sp.sqrt(root) + b) * (sp.sqrt(root) - b)
            simplified_expr = sp.simplify(expr)
            
            question = f"(√{root} + {b})(√{root} - {b})"
            solution = str(simplified_expr)        
            steps = [
                f"Folosim formula diferenței de pătrate: (a+b)(a-b) = a² - b²",
                f"Aici, a = √{root} și b = {b}",
                f"Înlocuim: (√{root})² - ({b})²",
                f"Simplificăm (√{root})² = {root}",
                f"Calculăm rezultatul final: {solution}"
            ]
        
        return self._create_exercise_dict(question, simplified_expr, steps)
        
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
                f"Mai întâi distribuim {a}: ({a} · {b}) + ({a} · √{c}) - {a}√{c}",
                f"Acum avem: {a*b} + {a}√{c} - {a}√{c}",
                f"Combinăm termenii asemenea cu √{c}",
                f"Termenii cu √{c} se anulează",
                f"Răspunsul final: {solution}"
            ]
            
            return self._create_exercise_dict(question, expr, steps)
    
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
        
                # Construct the expression symbolically
                expr = sp.simplify(sp.sqrt(a) * (b + c * sp.sqrt(a)) - b * sp.sqrt(a) + d)
                
                question = f"√{a}({b} + {c}√{a}) - {b}√{a} + {d}"
                solution = str(expr)
                
                steps = [
                    f"Mai întâi distribuim √{a}: (√{a} · {b}) + (√{a} · {c}√{a}) - {b}√{a} + {d}",
                    f"Simplificăm √{a} · √{a} = {a}",
                    f"Acum avem: {b}√{a} + {c}{a} - {b}√{a} + {d}",
                    f"Combinăm termenii asemenea cu √{a}",
                    f"Termenii cu √{a} se anulează",
                    f"Răspunsul final: {solution}"
                ]
            
            return self._create_exercise_dict(question, expr, steps)

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
                    f"Mai întâi dezvoltăm ({a} + √{b})²",
                    f"({a} + √{b})² = {a}² + 2·{a}·√{b} + (√{b})²",
                    f"Simplificăm (√{b})² = {b}",
                    f"Acum avem: {a*a} + 2·{a}·√{b} + {b} - 2·{a}·√{b}",
                    f"Termenii 2·{a}·√{b} se anulează",
                    f"Răspunsul final: {solution}"
                ]
                
                return self._create_exercise_dict(question, expr, steps)

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
                f"Mai întâi distribuim √{a} în primul termen: {c}√{a} - √{a}√{c}",
                f"Apoi distribuim √{c} în al doilea termen: √{c}√{a} - √{c}√{a*c}",
                f"Combinăm toți termenii: {c}√{a} - √{a}√{c} + √{c}√{a} - √{c}√{a*c}",
                f"Combinăm termenii asemenea cu √{a}√{c}",
                f"Simplificăm √{c}√{a*c} = √{c}·√{a*c} = √{a*c*c}",
                f"Răspunsul final: {solution}"
            ]
            
            return self._create_exercise_dict(question, expr, steps)
            
    
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
                    
                    # Construct the expression symbolically
                    expr = sp.simplify(c*a*sp.sqrt(b) + c*(d-a*sp.sqrt(b)))
                    
                    question = f"{c*a}√{b} + {c}({d}-{a}√{b})"
                    solution = str(expr)
                    
                    steps = [
                        f"Mai întâi distribuim {c} în al doilea termen: {c}·{a}·√{b} + {c}·{d} - {c}·{a}·√{b}",
                        f"Grupăm termenii asemenea cu {c}·{a}·√{b}",
                        f"Termenii {c}·{a}·√{b} se anulează",
                        f"Ne rămâne: {c}·{d}",
                        f"Răspunsul final: {solution}"
                    ]
                
                return self._create_exercise_dict(question, expr, steps)
    
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
                
                # Construct the expression symbolically
                expr = sp.simplify(c*a*sp.sqrt(b) + c*(d-sp.sqrt(b*a**2)))
                
                question = f"{c*a}·√{b} + {c}({d}-√{b*a**2})"
                solution = str(expr)
                
                steps = [
                    f"Mai întâi distribuim {c} în al doilea termen: {c}·{a}·√{b} + {c}·{d} - {c}·√{b*a**2}",
                    f"Simplificăm √{b*a**2} = {a}·√{b}",
                    f"Acum avem: {c}·{a}·√{b} + {c}·{d} - {c}·{a}·√{b}",
                    f"Termenii {c}·{a}·√{b} se anulează",
                    f"Ne rămâne: {c}·{d}",
                    f"Răspunsul final: {solution}"
                ]
            
            return self._create_exercise_dict(question, expr, steps)
    
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
                
                # Construct the expression symbolically
                expr = sp.simplify(sp.sqrt(a)*(b + c*sp.sqrt(a)) - b*sp.sqrt(a))
                
                question = f"√{a}({b}+{c}√{a}) - {b}√{a}"
                solution = str(expr)
                
                steps = [
                    f"Mai întâi distribuim √{a} în primul termen: {b}√{a} + {c}·{a} - {b}√{a}",
                    f"Termenii {b}√{a} se anulează",
                    f"Ne rămâne: {c}·{a}",
                    f"Răspunsul final: {solution}"
                ]
            
            return self._create_exercise_dict(question, expr, steps)
    
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
                    
                    # Construct the expression symbolically
                    expr = sp.simplify(sp.sqrt(a)*(c*sp.sqrt(a) + b) - b*sp.sqrt(a))
                    
                    question = f"√{a}({c}√{a} + {b}) - {b}√{a}"
                    solution = str(expr)
                    
                    steps = [
                        f"Mai întâi distribuim √{a} în primul termen: {c}·{a} + {b}√{a} - {b}√{a}",
                        f"Termenii {b}√{a} se anulează",
                        f"Ne rămâne: {c}·{a}",
                        f"Răspunsul final: {solution}"
                    ]                
                return self._create_exercise_dict(question, expr, steps)
    
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
                
                # Construct the expression symbolically
                sqrt_a2b = sp.sqrt(a**2 * b)
                expr = sp.expand((sqrt_a2b + c)*(a*sp.sqrt(b) - c))
                
                question = f"(√{(a**2)*b} + {c})({a}√{b} - {c})"
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
                
            return self._create_exercise_dict(question, expr, steps)
    
    def generate_type13(self) -> Dict:
        
            """
            Generates expression of form: (a + √b)² + (1 - a√b)²
            Returns: Dictionary with exercise details
            """
            solution = '-1'
            while int(solution) < 0 or int(solution) > 81:
                a = random.choice(self.nice_coefficients)
                b = random.choice(self.nice_roots)
                
                # Construct the expression symbolically
                sqrt_b = sp.sqrt(b)
                expr1 = (a + sqrt_b)**2
                expr2 = (1 - a*sqrt_b)**2
                expr = sp.expand(expr1 + expr2)
                
                question = f"({a} + √{b})² + (1 - {a}√{b})²"
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
            
            return self._create_exercise_dict(question, expr, steps)
    

    def generate_exercise(self, difficulty: int) -> Dict:
        """Generates radical expression exercises."""
        try:
            generator_method = getattr(self, f'generate_type{difficulty}')
            return generator_method()
        except AttributeError:
            raise ValueError(f"Invalid exercise type: {difficulty}")

    def _convert_to_latex(self, expr: Union[sp.Expr, str]) -> str:
        """
        Converts the expression to LaTeX format using SymPy.
        Handles both SymPy expressions and string inputs.
        """
        if isinstance(expr, str):
            return f"${expr}$"
        return f"${sp.latex(expr)}$"

    def _generate_hints(self, steps: List[str]) -> List[str]:
        """
        Generates comprehensive hints for the exercise.
        Provides general mathematical tips and specific solution steps.
        """
        general_hints = [
            
        ]
        return general_hints + steps  # Limit specific steps to avoid overwhelming hints

if __name__ == "__main__":
    # Create generator
    generator = RadicalExpressionGenerator()
    
    negative = 0
    negative_type = []
    too_big = 0
    too_big_type = []
    rep_count = 0
    rep_count_v = []
    tot = 0
    
# Generate existing types
    for exercise_type in range(1, 14):
        try:
            for i in range(1000):
                exercise = generator.generate_exercise(exercise_type)
                #print(f"\nType {exercise_type} Exercise:")
                if(int(exercise['solution']) > 100):
                    too_big += 1
                    too_big_type.append(exercise_type)
                if(int(exercise['solution']) < 0):
                    negative += 1
                    negative_type.append(exercise_type)
                if(exercise not in (rep_count_v)):
                    rep_count += 1
                    rep_count_v.append(exercise)
                    #print("Question:", exercise['question'])
                    #print("Solution:", exercise['solution'])
                
            print(f"Type {exercise_type}")
            print(f"Repetitions: {rep_count}")
            tot += rep_count
            rep_count = 0
        except ValueError as e:
            print(f"Could not generate type {exercise_type}: {e}")
                
    print(f"Too big: {too_big}")
    print(f"Negative: {negative}")
    print(f"Too big types: {too_big_type}")
    print(f"Negative types: {negative_type}")
    print(f"Total: {tot}")