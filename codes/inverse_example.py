import numpy as np
import matplotlib.pyplot as plt

N = 1000000
u = np.random.random(size=(N,))
x = 2*u - 1
plt.figure(figsize=(14, 7))
plt.hist(x, bins=50)
plt.title("Histogramme d'une variable aléatoire uniformément distribuée sur [-1, 1]")
plt.grid()
plt.show()