import numpy as np
import numpy.random as rnd
import matplotlib.pyplot as plt


def main():
    u = rnd.random()
    n = 1000
    u_array = rnd.random(1000)


def plot():
    x = 0.1
    i = 0
    qq = np.empty(199)
    qr = np.empty(199)
    while x <= 20:
        qq[i] = f(x)
        qr[i] = x
        x += 0.1
        i += 1
    plt.plot(qr, qq)
    plt.grid(linestyle=":", linewidth=1.5)
    plt.show()


def f(x):
    if x > 0:
        return (np.sqrt(5 / (2 * np.pi * (x ** 3)))) ** (
            (((-x - 5) ** 2) / (10 * x))
        )

    return 0


plot()
