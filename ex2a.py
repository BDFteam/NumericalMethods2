# DO NOT SEND THIS FILE BY E-MAIL!
# - Cemre

import numpy as np


def rmbrg():
    a = int(input("enter a: "))
    b = int(input("enter b: "))
    n = int(input("enter n: "))
    m = int(input("enter m: "))

    array = np.zeros((n, m), dtype=np.float128)
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

    for n in array:
        print(n)


def f(x) -> float:
    return 4 / (1 + (x ** 2))


rmbrg()
