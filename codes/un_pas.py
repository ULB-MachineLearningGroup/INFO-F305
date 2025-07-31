import numpy as np
import matplotlib.pyplot as plt

def equation_a_un_pas(f: callable, x0: float, steps: int = 5) -> None:
    x_s = [x0]
    
    for _ in range(steps):
        x_s.append(f(x_s[-1]))
    
    l1 = np.arange(-4, 4, 0.1)
    l2 = f(l1)
    
    plt.figure(figsize=(8, 8))
    plt.plot(l1, l2, label="x(k+1) = f(x(k))")
    plt.plot(l1, l1, label="x(k+1) = x(k)", linestyle="dashed")

    plt.vlines(x=x_s[0], ymin=0, ymax=f(x_s[0]), color="green")
    plt.plot([x_s[0], x_s[1]], [x_s[1], x_s[1]], color="green")
    for x in range(1, len(x_s)-1):
        plt.vlines(x=x_s[x], ymin=x_s[x], ymax=f(x_s[x]), color="green")
        plt.plot([x_s[x], x_s[x+1]], [x_s[x+1], x_s[x+1]], color="green")
    
    plt.xlabel("x(k)")
    plt.ylabel("x(k+1)")
    plt.grid()
    plt.legend()