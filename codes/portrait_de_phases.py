import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

def portrait_de_phase(A):
    plt.figure(figsize=(12, 12))
    vecteurs_flux(A)
    vecteurs_propres(A)
    isoclines(A)
    vecteurs_vitesse(A)
    for _ in range(4):
        trajectoire(A, [0, 5], np.random.random(2)*3-1.5)
    plt.title("Portrait de phases complet")