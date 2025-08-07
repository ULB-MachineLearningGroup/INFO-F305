import numpy as np

sample = []
N = 1000000
C = 1

def p(x):
    return np.sin(x) if (0<=x<=np.pi or 2*np.pi<=x<=3*np.pi) else 0

while len(sample) < N:
    x = np.random.uniform(0, 3*np.pi)
    u = np.random.uniform()
    if u <= np.sin(x)/C:
        sample.append(x)

plt.figure(figsize=(10, 7))
plt.hist(sample, bins=200)
plt.title("Histogramme de l'échantillon obtenu par la méthode du rejet")
plt.grid()
plt.tight_layout()
plt.show()