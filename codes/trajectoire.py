import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

def trajectoire(A: list[list], interval: list[int], c_i: list[int]) -> None:
    def xdot(t, x):
        return A @ x

    sol = solve_ivp(
        xdot, interval, c_i,
        t_eval=np.linspace(interval[0], interval[1], 250)
    )

    plt.plot(sol.y[0, :], sol.y[1, :], label="Trajectoire ("+r"$\dot{x}(0)$"+f" = {c_i})")
    plt.title(f"Trajectoire demarrant en {interval}")
    plt.xlabel("x1")
    plt.ylabel("x2")
    plt.legend()
    plt.grid()