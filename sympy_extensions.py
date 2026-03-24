import sympy as sp

def solve_with_evalf(*args, **kwargs):
    sol = sp.solve(*args, **kwargs)
    return {k: v.evalf() for k, v in sol.items()}