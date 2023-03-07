from sys import stdin

samples = [
    (
        # Sample Input 1
        """10
6
""",
        # Sample Output 1
        """1
"""
    ),
    (
        # Sample Input 2
        """9
-13
""",
        # Sample Output 2
        """4
"""
    ),
]


def solve(problem_input: str):
    x, y = [int(line) for line in problem_input.splitlines()]
    if x > 0 and y > 0:  # NE
        return 1
    elif y > 0:  # SE
        return 2
    elif x > 0:  # NW
        return 4
    else:  # SW
        return 3


if __name__ == "__main__":
    print(solve(stdin.read()))
