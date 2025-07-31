import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

def vecteurs_propres(A):
    L, V = np.linalg.eig(A)
    line_range = np.linspace(-1.5, 1.5, 100)
    V = np.real(V)
    if V[0, 0] != 0:
        eigenvector_1 = (V[1,0] / V[0, 0]) * line_range
        plt.plot(line_range, eigenvector_1, color="green", label='v_1')
    if V[0, 1] != 0:
        eigenvector_2 = (V[1,1] / V[0, 1]) * line_range
        plt.plot(line_range, eigenvector_2, color="green", label='v_2')
    if V[0, 0] != 0 and V[0, 1] != 0:
        plt.quiver([0, 0], [0, 0], V[0, :], V[1, :], angles='xy', scale_units='xy', scale=1, linewidth=2, color='darkgreen')
    
    plt.legend()
    
    plt.title("Vecteurs propres")
    plt.xlim([-1.5, 1.5])
    plt.ylim([-1.5, 1.5])
    plt.grid()