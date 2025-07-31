import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt

c = 2

def xdot(t, x):
    return [1 - c * x[0]]
    
sol = solve_ivp(xdot, [0, 10], [1], t_eval=np.linspace(0, 10, 100))

plt.figure(figsize=(8, 6))
plt.plot(sol.t, sol.y[0])
plt.xlabel('Temps')
plt.ylabel('x(t)')
plt.title('Resolution avec retard')
plt.grid()
plt.show()