import numpy as np
import matplotlib.pyplot as plt

def equation_lineaire_affine_a_un_pas(a: float, b: float, x0: float, steps: int = 5) -> None:
    x_s = [x0]
    
    for _ in range(steps):
        x_s.append(a*x_s[-1]+b)
    
    l1 = np.arange(0, 12)
    l2 = a*l1+b
    
    plt.figure(figsize=(8, 8))
    plt.plot(l1, l2, label=f"x(k+1) = {a}x(k)+{b}")
    plt.plot(l1, l1, label=f"x(k+1) = x(k)", linestyle="dashed")
    
    for x in range(len(x_s)-1):
        plt.vlines(x=x_s[x], ymin=x_s[x], ymax=a*x_s[x]+b, color="green")
        plt.plot([x_s[x], x_s[x+1]], [x_s[x+1], x_s[x+1]], color="green")
    
    plt.xlabel("x(k)")
    plt.ylabel("x(k+1)")
    plt.grid()
    plt.legend()