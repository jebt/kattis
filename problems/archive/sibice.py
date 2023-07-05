import math
from sys import stdin

# noinspection LongLine
samples = [
    (
        # Input 1
        """5 3 4\n3\n4\n5\n6\n7\n""",
        # Output 1
        """DA\nDA\nDA\nNE\nNE\n"""
    ),
    (
        # Input 2
        """2 12 17\n21\n20\n""",
        # Output 2
        """NE\nDA\n"""
    ),
]


def solve(problem_input: str):
    lines = problem_input.splitlines()
    n, l, w = [int(x) for x in lines[0].split()]
    diameter = math.sqrt(l * l + w * w)
    out = ""
    for match in lines[1::]:
        if int(match) <= diameter:
            out += "DA\n"
        else:
            out += "NE\n"
    return out.strip()


if __name__ == "__main__":
    print(solve(stdin.read()))
