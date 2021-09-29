# DO NOT SEND THIS FILE BY E-MAIL!
# - Cemre
from typing import Callable

import numpy as np


def rmbrg(
    function: Callable[[float], float],
    left_boundry: float = 0,
    right_boundry: float = 0,
    n: int = 0,
    m: int = 0,
):
    left_boundry = (
        left_boundry
        if left_boundry is not None
        else int(input("enter left boundry: "))
    )
    right_boundry = (
        left_boundry
        if right_boundry is not None
        else int(input("enter right boundry: "))
    )
    n = n if n is not None else int(input("enter n: "))
    m = m if m is not None else int(input("enter m: "))

    matrix = np.zeros((n, m), dtype=np.longdouble)
    matrix[0][0] = (
        0.5
        * (right_boundry - left_boundry)
        * (function(left_boundry) + function(right_boundry))
    )

    for i in range(n):
        if i != 0:
            sum = 0
            for j in range((2 ** (i - 1))):
                sum += function(
                    left_boundry
                    + ((2 * (j + 1)) - 1)
                    * ((right_boundry - left_boundry) / (2 ** i))
                )
            matrix[i][0] = (0.5 * matrix[i - 1][0]) + (
                (((right_boundry - left_boundry) / (2 ** i))) * sum
            )

        for j in range(min(m, i + 1)):
            if i != 0 and j != 0:
                matrix[i][j] = matrix[i][j - 1] + (1 / ((4 ** j) - 1)) * (
                    matrix[i][j - 1] - matrix[i - 1][j - 1]
                )

    return matrix


# def f(x: float) -> float:
#     return 4 / (1 + (x ** 2))


def main():
    print(rmbrg(lambda x: 4 / (1 + (x ** 2))))


if __name__ == "__main__":
    main()
