import numpy as np
import matplotlib.pyplot as plt

def vecteurs_flux(A):
    x1, x2 = np.meshgrid(np.arange(-1.5, 1.6, 0.1), np.arange(-1.5, 1.6, 0.1))
    
    x1_values = A[0,0]*x1 + A[0,1]*x2
    x2_values = A[1,0]*x1 + A[1,1]*x2
    
    plt.streamplot(x1, x2, x1_values, x2_values, density=0.4, linewidth=0.2, color="black")

plt.figure(figsize=(figsize, figsize))
vecteurs_flux(np.array([[1, -2], [-2, 1]]))
plt.xlim([-1.5, 1.5])
plt.ylim([-1.5, 1.5])
plt.xlabel("x1")
plt.ylabel("x2")
plt.grid()

plt.savefig("vecteurs_flux.jpg", dpi=200, bbox_inches='tight')
plt.show()