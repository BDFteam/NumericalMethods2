from typing import Callable

import numpy as np
import matplotlib.pyplot as plt

f = lambda x: 1 / (x + 1)


def rmbrg(a: float, b: float, n: int, m: int):
    array = np.zeros((n, m))
    array[0][0] = 0.5 * (b - a) * (f(a) + f(b))

    for i in range(n):
        if i != 0:
            sum = 0
            for k in range((2 ** (i - 1))):
                sum += f(a + ((2 * (k + 1)) - 1) * ((b - a) / (2 ** i)))
            array[i][0] = (0.5 * array[i - 1][0]) + (
                (((b - a) / (2 ** i))) * sum
            )

        for j in range(min(m, i + 1)):
            if i != 0 and j != 0:
                array[i][j] = array[i][j - 1] + (1 / ((4 ** j) - 1)) * (
                    array[i][j - 1] - array[i - 1][j - 1]
                )

    return array


other_F = lambda x: rmbrg(0, x, 20, 20)[-1, -1]
F = lambda x: np.log(x + 1)


def main():
    array = np.linspace(0, 10, 100)
    values_F = np.zeros(100)
    values_OTHER_F = np.zeros(100)

    for i in range(100):
        values_F[i] = F(array[i])
        values_OTHER_F[i] = other_F(array[i])
        print(i + 1)

    plt.plot(array, values_F)
    plt.plot(array, values_OTHER_F)
    plt.show()


if __name__ == "__main__":
    main()
