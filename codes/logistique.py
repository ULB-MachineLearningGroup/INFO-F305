import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt

c = 0.2
k = 1.5

def xdot(t, x):
    return [(c * x[0])*(1-x[0]/k)]

sol = solve_ivp(xdot, [0, 50], [0.3], t_eval=np.linspace(0, 50, 100))

plt.figure(figsize=(8, 6))
plt.plot(sol.t, sol.y[0])
plt.xlabel('Temps')
plt.ylabel('x(t)')
plt.title('Croissance logistique')
plt.grid()
plt.show()