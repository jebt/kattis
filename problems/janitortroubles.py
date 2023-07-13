import math
from functools import reduce
from sys import stdin

# noinspection LongLine
samples = [
    (
        # Input 1
        """3 3 3 3\n""",
        # Output 1
        """9\n"""
    ),
    (
        # Input 2
        """1 2 1 1\n""",
        # Output 2
        """1.299038105676658\n"""
    ),
    (
        # Input 3
        """2 2 1 4\n""",
        # Output 3
        """3.307189138830738\n"""
    ),
]


def solve(problem_input: str):
    sides: list[int | float] = [int(x) for x in problem_input.split()]
    semiperimeter = sum(sides) / 2

    sides[0] = semiperimeter - sides[0]
    num = math.sqrt(reduce(lambda x, y: x * (semiperimeter - y), sides))

    # num = math.sqrt((semiperimeter - sides[0]) * (semiperimeter - sides[1]) * (semiperimeter - sides[2]) * (
    #             semiperimeter - sides[3]))

    # total = 1
    # for side in sides:
    #     total *= (semiperimeter - side)
    # num = math.sqrt(total)

    if num % 1 == 0:
        num = int(num)
    return num


if __name__ == "__main__":
    print(solve(stdin.read()))
