import numpy as np
import numpy.random as rnd
import matplotlib.pyplot as plt
from scipy.integrate import quad
from scipy.optimize import ridder
from scipy.stats import describe

# print(rmbrg(a, b, n, m, lambda x: 4 / (1 + (x ** 2))))


def main():
    # plot()

    n = 1000
    u_array = rnd.random(1000)
    a_array = np.empty(n)

    for i in range(n):
        a_array[i] = simulatesample(u_array[i])

    # plt.hist(a_array, 20, range=(0, 20))
    # plt.show()

    print(describe(a_array))


def plot():
    x_array = np.linspace(0.1, 20, 1000)
    y_array = np.empty(1000)
    for i, x in enumerate(x_array):
        y_array[i] = f(x)
        x_array[i] = x
    plt.plot(x_array, y_array)
    plt.xlim([0, 20])
    plt.grid(linestyle=":", linewidth=1.5)
    plt.show()


def f(x):
    if x > 0:
        part1 = np.sqrt(5 / (2 * np.pi * (x ** 3)))
        part2 = -(((x - 5) ** 2) / (10 * x))
        return part1 * np.exp(part2)
    return 0


def F(x):
    return quad(f, -np.inf, x)[0]


def simulatesample(u: float):
    find_root_of = lambda x: F(x) - u
    return ridder(find_root_of, 0, 100)


if __name__ == "__main__":
    main()
