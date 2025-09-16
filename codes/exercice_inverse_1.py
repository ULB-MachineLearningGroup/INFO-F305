from sympy import solve, symbols, lambdify
import numpy as np

def inverse(repartition, u):
    u_sym = symbols('u')
    return lambdify(u_sym, solve(repartition - u_sym, symbols('x'))[0], 'numpy')(u)

repartition = 2*symbols('x')-symbols('x')**2
u = np.array([0.75, 0.43, 0.39, 0.65, 0.17])
print(inverse(repartition, u))

# Sortie:
# [0.5 0.24501656 0.21897503 0.40839202 0.08895664]