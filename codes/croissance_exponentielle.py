import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt

c = 0.1

def xdot(t, x):
    return [c * x[0]]

sol = solve_ivp(
    xdot, [0, 10], [1],
    t_eval=np.linspace(0, 10, 100)
)

plt.figure(figsize=(8, 6))
plt.plot(sol.t, sol.y[0])
plt.xlabel('Temps')
plt.ylabel('x(t)')
plt.title('Exemple 2: Croissance exponentielle')
plt.grid()
plt.show()