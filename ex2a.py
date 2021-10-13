from typing import Callable
import numpy as np

f = lambda x: 4 / (1 + (x ** 2))

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


def main():
    a = 0
    b = 1
    n = 6 
    m = 6
    print(rmbrg(a,b,n,m))


if __name__ == "__main__":
    main()
