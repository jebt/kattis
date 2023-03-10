from sys import stdin

samples = [
    (
        # Input 1
        """3
5 -10 15
""",
        # Output 1
        """1
"""
    ),
    (
        # Input 2
        """5
-14 -5 -39 -5 -7
""",
        # Output 2
        """5
"""
    ),
]


def solve(problem_input: str):
    return [int(part) < 0 for part in problem_input.split()].count(True)


if __name__ == "__main__":
    print(solve(stdin.read()))
