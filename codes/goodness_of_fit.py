import numpy as np
from scipy.stats import kstest

N = 10000
s = 25

generator = LGC()
numbers = np.array([generator() for _ in range(N)])

D, p_value = kstest(numbers, 'uniform')

print("On rejette l'hypothèse d'uniformité:", p_value < 0.05)

# Sortie:
# On rejette l'hypothèse d'uniformité: False