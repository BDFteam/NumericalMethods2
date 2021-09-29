# DO NOT SEND THIS FILE BY E-MAIL!
# - Cemre
from typing import Callable

import numpy as np


def rmbrg(
    left_boundry: float,
    right_boundry: float,
    n: int,
    m: int,
    function: Callable[[float], float],
):
    array = np.zeros((n, m), dtype=np.longdouble)
    array[0][0] = (
        0.5
        * (right_boundry - left_boundry)
        * (function(left_boundry) + function(right_boundry))
    )

    for i in range(n):
        if i != 0:
            sum = 0
            for k in range((2 ** (i - 1))):
                sum += function(
                    left_boundry
                    + ((2 * (k + 1)) - 1)
                    * ((right_boundry - left_boundry) / (2 ** i))
                )
            array[i][0] = (0.5 * array[i - 1][0]) + (
                (((right_boundry - left_boundry) / (2 ** i))) * sum
            )

        for j in range(min(m, i + 1)):
            if i != 0 and j != 0:
                array[i][j] = array[i][j - 1] + (1 / ((4 ** j) - 1)) * (
                    array[i][j - 1] - array[i - 1][j - 1]
                )

    return array


def g(x: float) -> float:
    return 4 / (1 + (x ** 2))


def main():
    a = int(input("enter a: "))
    b = int(input("enter b: "))
    n = int(input("enter n: "))
    m = int(input("enter m: "))

    print(rmbrg(a, b, n, m, g))


if __name__ == "__main__":
    main()
