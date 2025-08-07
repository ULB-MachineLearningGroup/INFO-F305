import numpy as np
import scipy as sp

generator = LGC()
numbers = np.array([generator() for _ in range(1000000)])

print("Valeurs Théoriques")
print(f"Moment 1: {1/2}, Moment 2: {1/3}, Moment 3: {1/4}")
print("Estimations")
print(f"Moment 1: {np.mean(numbers)}")
print(f"Moment 2: {np.mean(numbers**2)}")
print(f"Moment 3: {np.mean(numbers**3)}")

# Sortie
# Valeurs Théoriques
# Moment 1: 0.5, Moment 2: 0.3333333333333333, Moment 3: 0.25
# Estimations
# Moment 1: 0.5004244952586155
# Moment 2: 0.33372665650472605
# Moment 3: 0.2503335322416548