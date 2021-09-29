import numpy as np
import numpy.random as rnd
import matplotlib.pyplot as plt

from ex2a import rmbg
# print(rmbrg(a, b, n, m, lambda x: 4 / (1 + (x ** 2))))


def main():
    u = rnd.random()
    n = 1000
    u_array = rnd.random(1000)
    simulatesample(u)
    # plot()


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
    plt.xlim([0, 10])
    plt.ylim([0, 3])
    plt.grid(linestyle=":", linewidth=1.5)
    plt.show()


def f(x):
    if x > 0:
        part1 = (5 / (2 * np.pi * x ** 3)) ** 0.5
        part2 = (-((x - 5) ** 2)) / (10 * x)
        return part1 ** part2
    return 0


def simulatesample(u):
    big_f = ?
    big_f_solvable = big_f - u
    


if __name__ == "__main__":
    main()
