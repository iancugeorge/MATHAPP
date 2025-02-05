import random
from fractions import Fraction
import sympy as sp
from typing import Dict, Optional, List, Union
import re

class AritmeticFractiiGenerator:
    def __init__(self, seed: Optional[int] = None):
        """Inițializează generatorul cu un seed opțional pentru reproducibilitate."""
        if seed is not None:
            random.seed(seed)
        self.fractii_pedagogice = [
            (1, 2), (1, 3), (1, 4), (2, 3), (3, 4), (1, 5),
            (2, 5), (3, 5), (4, 5), (1, 6), (5, 6), (1, 8),
            (3, 8), (5, 8), (7, 8), (1, 10), (3, 10), (7, 10)
        ]
        self.rezultate_pedagogice = [0, 1, 2, 3, 4, 5, 6, 7, 10]


    def convert_string_to_latex(self, raw_string: str) -> str:
        """
        Convertește șirul de caractere omenește într-un șir LaTeX.
        Aplică transformări pentru operatori matematici, fracții și perechi de paranteze.
        """
        # Înlocuim operatorii de bază
        latex_str = raw_string.replace("·", r"\cdot")
        latex_str = latex_str.replace(":", r"\div")
        
        # Convertim fracțiile de forma a/b în formatul LaTeX
        # Această abordare caută secvențe de cifre separate de '/'.
        latex_str = re.sub(r'(\d+)/(\d+)', r'\\frac{\1}{\2}', latex_str)
        
        # Înlocuim perechile complete de paranteze cu \left( și \right)
        # Această regulă se aplică pentru parantezele care nu conțin alte paranteze (nu sunt imbricate).
        latex_str = re.sub(r'\(([^()]*)\)', r'\\left(\1\\right)', latex_str)
        
        return f"{latex_str}"

    
    def _create_exercise_dict(self, question_str: str, solution: Union[int, Fraction], steps: List[str]) -> Dict:
        """
        Creează dicționarul standardizat pentru exercițiu.
        Include întrebarea originală, soluția ca șir și soluția în LaTeX.
        """
        sol_expr = sp.nsimplify(solution)
        return {
            "type": "aritmetic_fractii",
            "difficulty": len(steps) - 2,
            "question": question_str,
            "questionLatex": self.convert_string_to_latex(question_str),
            "solution": str(solution),
            "solutionLatex": sp.latex(sol_expr),
            "hints": self._generate_hints(steps)
        }

    def _generate_hints(self, steps: List[str]) -> List[str]:
        """
        Generează indicii pentru exercițiu, combinând sfaturi generale cu pașii specifici.
        """
        sfaturi_generale = [
            "Încercați să transformați toate numerele la aceeași reprezentare.",
            "Verificați dacă există factori comuni sau modele între fracții."
        ]
        return sfaturi_generale + steps

    def format_number(self, num: Union[int, float, Fraction], style: str = 'fraction') -> str:
        """
        Formatează numerele pentru afișare.
        Dacă numărul este o fracție ce poate fi reprezentată ca întreg, se afișează ca întreg,
        altfel în forma a/b.
        """
        if isinstance(num, (int, float)):
            num = Fraction(num).limit_denominator(100)
        if style == 'decimal':
            valoare = float(num)
            if valoare.is_integer():
                return str(int(valoare))
            return f"{valoare:.3f}".rstrip('0').rstrip('.')
        if num.denominator == 1:
            return str(num.numerator)
        return f"{num.numerator}/{num.denominator}"

    def get_nice_fraction(self, exclude: Optional[Fraction] = None) -> Fraction:
        """
        Returnează o fracție pedagogică, excluzând o anumită valoare, dacă este specificată.
        """
        while True:
            num, den = random.choice(self.fractii_pedagogice)
            frac = Fraction(num, den)
            if exclude is None or frac != exclude:
                return frac

    def get_target_result(self) -> Union[int, Fraction]:
        """
        Returnează rezultatul țintă pentru exercițiu.
        Cu 80% șanse rezultatul este un număr întreg, altfel o fracție.
        """
        if random.random() < 0.8:
            return random.choice(self.rezultate_pedagogice)
        return self.get_nice_fraction()

    def generate_type1(self) -> Dict:
        """
        Generează exercițiu de tipul:
        (f1 + f2) · m
        unde m se calculează astfel încât rezultatul final să fie egal cu rezultatul țintă.
        """
        target = self.get_target_result()
        frac1 = self.get_nice_fraction()
        frac2 = self.get_nice_fraction()
        suma = frac1 + frac2
        multiplier = Fraction(target) / suma

        question_str = f"({self.format_number(frac1)} + {self.format_number(frac2)}) · {self.format_number(multiplier)}"
        steps = [
            f"Mai întâi adunăm fracțiile: {self.format_number(frac1)} + {self.format_number(frac2)}",
            f"Suma este: {self.format_number(suma)}",
            f"Calculăm factorul de multiplicare: {self.format_number(multiplier)}",
            f"Înmulțim suma cu factorul: {self.format_number(suma)} · {self.format_number(multiplier)}",
            f"Răspunsul final: {self.format_number(target)}"
        ]
        return self._create_exercise_dict(question_str, target, steps)

    def generate_type2(self) -> Dict:
        """
        Generează exercițiu de tipul:
        (f1 - f2) : f3
        unde rezultatul final este egal cu rezultatul țintă.
        """
        target = self.get_target_result()
        frac1 = self.get_nice_fraction()
        frac2 = self.get_nice_fraction()
        frac3 = self.get_nice_fraction()
        diferenta = frac1 - frac2
        rezultat = diferenta / frac3

        question_str = f"({self.format_number(frac1)} - {self.format_number(frac2)}) : {self.format_number(frac3)}"
        steps = [
            f"Calculăm diferența dintre fracții: {self.format_number(frac1)} - {self.format_number(frac2)}",
            f"Diferența este: {self.format_number(diferenta)}",
            f"Împărțim diferența la: {self.format_number(frac3)}",
            f"Rezultatul este: {self.format_number(diferenta)} : {self.format_number(frac3)}",
            f"Răspunsul final: {self.format_number(target)}"
        ]
        return self._create_exercise_dict(question_str, target, steps)

    def generate_exercise(self, difficulty: int) -> Dict:
        """
        Generează exerciții de aritmetică cu fracții.
        difficulty = 1: operații simple (adunare și înmulțire)
        difficulty = 2: operații mai complexe (scădere și împărțire)
        """
        try:
            generator_method = getattr(self, f'generate_type{difficulty}')
            return generator_method()
        except AttributeError:
            raise ValueError(f"Tipul de exercițiu invalid: {difficulty}")

Generator = AritmeticFractiiGenerator