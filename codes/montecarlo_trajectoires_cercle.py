import numpy as np
from scipy.integrate import solve_ivp

def trajectoire(A, interval, c_i):
    def xdot(t, x):
        return A @ x

    return solve_ivp(xdot, interval, c_i, t_eval=np.linspace(interval[0], interval[1], 250)).y[:, -1]

n_trajectoires = 10
c_i = (10*np.random.random((n_trajectoires, 2)))-5
rayons = (c_i[:, 0]**2 + c_i[:, 1]**2)**0.5

t = [0, 100]
position_finale = np.array([trajectoire(np.array([[0, 1], [-1, 0]]), t, i) for i in c_i])
rayons_finaux = (position_finale[:, 0]**2 + position_finale[:, 1]**2)**0.5

devies = np.abs(rayons-rayons_finaux) >= 10e-3
proportion = np.sum(devies/n_trajectoires)

print(f"Probabilité de se trouver hors du cercle initial: {proportion}")

# Sortie:
# Probabilité de se trouver hors du cercle initial: 0.0