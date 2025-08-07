import numpy as np

sample = []
N = 500000
C = (3**(1/3))**2

while len(sample) < N:
    x = np.random.uniform(0, 3**(1/3))
    u = np.random.uniform()
    if u <= (x**2)/C:
        sample.append(x)

plt.figure(figsize=(7, 7))
plt.hist(sample, bins=100)
plt.title("Histogramme de l'échantillon obtenu par la méthode du rejet")
plt.grid()
plt.tight_layout()
plt.show()