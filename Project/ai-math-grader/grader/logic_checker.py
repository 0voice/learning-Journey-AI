from sympy import sympify, simplify
from sympy.core.sympify import SympifyError

def compare_answers(expected, actual):
    try:
        exp = simplify(sympify(expected))
        act = simplify(sympify(actual))
        return {"correct": exp == act}
    except SympifyError:
        return {"correct": expected.strip() == actual.strip()}
