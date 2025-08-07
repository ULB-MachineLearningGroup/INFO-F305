import numpy as np
import scipy as sp
from scipy.stats import chi2

N = 10000
s = 25

generator = LGC()
numbers = np.array([generator() for _ in range(N)])

counts, _ = np.histogram(numbers, bins=s, range=(0, 1))

expected = N / s
chi_stat = s/N * np.sum((counts - expected)**2)
p_value = 1 - chi2.cdf(chi_stat, df=s-1)

print("On rejette l'hypothèse d'uniformité:", p_value < 0.05)

# Sortie:
# On rejette l'hypothèse d'uniformité: False