from sympy import solve, symbols, lambdify
import numpy as np

def inverse(repartition, u):
    u_sym = symbols('u')
    return lambdify(u_sym, solve(repartition - u_sym, symbols('x'))[0], 'numpy')(u)

repartition = (symbols('x')+1)/2
u = np.random.random(size=(5,))
x = inverse(repartition, u)
print(u)
print(x)

# Sortie:
# [0.40169548 0.77292057 0.50537528 0.35168255 0.39918269]
# [-0.19660905  0.54584114  0.01075057 -0.29663491 -0.20163462]