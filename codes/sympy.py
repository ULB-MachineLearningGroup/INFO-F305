import sympy as sp
import numpy as np
import matplotlib.pyplot as plt

t = sp.symbols('t')
x1, x2 = sp.symbols('x1 x2')
X = sp.Matrix([x1, x2])

A = sp.Matrix([[1, 2],
               [2, 1]])

eigen_values = A.eigenvals()
eigen_vectors = A.eigenvects()

c1, c2 = sp.symbols('c1 c2')
solutions = c1 * sp.exp(list(eigen_values.keys())[0] * t) * eigen_vectors[0][2][0] + \
            c2 * sp.exp(list(eigen_values.keys())[1] * t) * eigen_vectors[1][2][0]

init_conditions = {solutions[0].subs(t, 0): 0.5, solutions[1].subs(t, 0): 0}
constants = sp.solve([eq for eq in init_conditions], [c1, c2])

x1_t = solutions[0].subs(constants)
x2_t = solutions[1].subs(constants)