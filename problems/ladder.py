import math
from sys import stdin

# noinspection LongLine
samples = [
    (
        # Input 1
        """500 70\n""",
        # Output 1
        """533\n"""
    ),
    (
        # Input 2
        """1000 10\n""",
        # Output 2
        """5759\n"""
    ),
]


def solve(problem_input: str):
    h, v = [int(x) for x in problem_input.split()]
    rad = v * math.pi / 180
    return math.ceil(h / math.sin(rad))


if __name__ == "__main__":
    print(solve(stdin.read()))
