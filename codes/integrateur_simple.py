import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt

c = 1

def xdot(t, x):
    return [c * np.sin(t)]

condition_initiale = [1]
temps_simulation = [0, 10]

sol = solve_ivp(
    xdot, temps_simulation, condition_initiale,
    t_eval=np.linspace(
        temps_simulation[0], temps_simulation[1], 100
    )
)

plt.figure(figsize=(8, 6))
plt.plot(sol.t, sol.y[0])
plt.xlabel('Temps')
plt.ylabel('x(t)')
plt.title('Exemple 1: Systeme simple')
plt.grid()
plt.show()