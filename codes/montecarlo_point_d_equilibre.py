import numpy as np
from scipy.integrate import solve_ivp

def trajectoire(A, interval, c_i):
    def xdot(t, x):
        return A @ x

    return solve_ivp(xdot, interval, c_i, t_eval=np.linspace(interval[0], interval[1], 250)).y[:, -1]

n_trajectoires = 1000
c_i = (10*np.random.random((n_trajectoires, 2)))-5
t = [0, 100]
position_finale = np.array([trajectoire(np.array([[0, 1], [-1, -1]]), t, i) for i in c_i])
print(f"Position moyenne finale: {np.mean(position_finale, axis=0)}")
print(f"Variance de la position finale: {np.std(position_finale, axis=0)**2}")

# Sortie:
# Position moyenne finale: [-2.31221753e-08  1.38081782e-08]
# Variance de la position finale: [2.00299502e-13 1.68805031e-13]