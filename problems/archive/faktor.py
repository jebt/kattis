import math
from sys import stdin

samples = [
    (
        # Input 1
        """38 24\n""",
        # Output 1
        """875\n"""
    ),
    (
        # Input 2
        """1 100\n""",
        # Output 2
        """100\n"""
    ),
    (
        # Input 3
        """10 10\n""",
        # Output 3
        """91\n"""
    ),
]


def solve(problem_input: str):
    articles, impact_factor = [int(x) for x in problem_input.split()]
    citations = articles * (impact_factor - 1)
    if citations % 1 == 0:
        citations += 1
    else:
        citations = math.ceil(citations)
    return citations


if __name__ == "__main__":
    print(solve(stdin.read()))
