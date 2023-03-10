from sys import stdin

samples = [
    (
        # Input 1
        """1 1
""",
        # Output 1
        """0.5
"""
    ),
    (
        # Input 2
        """2 2
""",
        # Output 2
        """2
"""
    ),
]


def solve(problem_input: str):
    sides = [int(x) for x in problem_input.split()]
    area = (sides[0] * sides[1]) / 2
    if area.is_integer():
        return int(area)
    return area


if __name__ == "__main__":
    print(solve(stdin.read()))
