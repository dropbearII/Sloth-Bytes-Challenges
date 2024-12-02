"""
Weekly Challenge 2024-11-26

Splitting Up Numbers

Create a function that takes a number num and returns each place value in the number.

Examples

num_split(39)
output =[30, 9]

num_split(-434)
output = [-400, -30, -4]

num_split(100)
output =[100, 0, 0]
"""
import numpy as np


def num_split(num: int) -> list:
    if num < 0:
        sign = -1
    else:
        sign = 1
    num_list: list[int] = list(map(int, str(abs(num))))
    digits = np.array(num_list)
    powers_of_tens = np.fromfunction(lambda i: 10 ** i, (digits.size,), dtype=int)
    digits = digits * np.flip(powers_of_tens) * sign
    return digits.tolist()


if __name__ == '__main__':
    print(f'39 is split into: ', num_split(39))
    print(f'-434 is split into: ', num_split(-434))
    print(f'100 is split into: ', num_split(100))
