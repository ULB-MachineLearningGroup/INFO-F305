import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt

def isoclines(A):
    line_range = np.linspace(-1.5, 1.5, 100)
    if A[0, 1] != 0:
        isocline_1 = -(A[0, 0] / A[0, 1]) * line_range
        plt.plot(line_range, isocline_1, color='blue', label='Isocline 1')
    if A[1, 1] != 0:
        isocline_2 = -(A[1, 0] / A[1, 1]) * line_range
        plt.plot(line_range, isocline_2, color='blue', label='Isocline 2')
    
    plt.legend()
    plt.title("Isoclines du systeme A")
    plt.xlim([-1.5, 1.5])
    plt.ylim([-2.5, 2.5])
    plt.grid()