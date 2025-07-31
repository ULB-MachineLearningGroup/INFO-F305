import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt

# Les fonction vecteurs_propres(A) et vecteurs_vitesse(A) ont deja ete definies
def trajectoire(A, interval, c_i):
    def xdot(t, x):
        return A @ x
    sol = solve_ivp(xdot, interval, c_i, t_eval=np.linspace(interval[0], interval[1], 250))
    plt.plot(sol.y[0, :], sol.y[1, :], label=f"Trajectoire (x(0) = {c_i})")

A = np.array([[3, 1], [1, 3]])
plt.figure(figsize=(12, 12))
vecteurs_propres(A)
vecteurs_vitesse(A)
trajectoire(A, [0, 3], [0, 1])
trajectoire(A, [0, 3], [-0.5, -1])
plt.xlim([-1.5, 1.5])
plt.ylim([-1.5, 1.5])
plt.xlabel("x1")
plt.ylabel("x2")
plt.grid()
plt.legend()
plt.tight_layout()
plt.show()