import numpy as np
import matplotlib.pyplot as plt

def equation_a_un_pas(f: callable, x0: float, steps: int = 5, xmin: int = -4, xmax: int = 4, label_space: float = 0.5) -> None:
    x_s = [x0]
    
    for _ in range(steps):
        x_s.append(f(x_s[-1]))
    
    l1 = np.arange(xmin, xmax, 0.01)
    l2 = f(l1)
    
    plt.figure(figsize=(8, 8))
    plt.plot(l1, l2, label="x(k+1) = f(x(k))")
    plt.plot(l1, l1, label="x(k+1) = x(k)", linestyle="dashed")

    plt.vlines(x=x_s[0], ymin=0, ymax=f(x_s[0]), color="green")
    plt.plot([x_s[0], x_s[1]], [x_s[1], x_s[1]], color="green")
    plt.text(x_s[0], x_s[1] - label_space, f"x(0)", ha='center', va='top', fontsize=8, color="blue")
    for x in range(1, len(x_s)-1):
        plt.vlines(x=x_s[x], ymin=x_s[x], ymax=f(x_s[x]), color="green")
        plt.plot([x_s[x], x_s[x+1]], [x_s[x+1], x_s[x+1]], color="green")
        plt.text(x_s[x], x_s[x] - label_space, f"x({x})", ha='center', va='top', fontsize=8, color="blue")
    
    plt.xlabel("x(k)")
    plt.ylabel("x(k+1)")
    plt.grid()
    plt.legend()