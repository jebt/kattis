from sys import stdin

samples = [
    (
        # Input 1
        """11
""",
        # Output 1
        """11
"""
    ),
    (
        # Input 2
        """42
""",
        # Output 2
        """24
"""
    ),
]


def solve(problem_input: str):
    return problem_input[1] + problem_input[0]


if __name__ == "__main__":
    print(solve(stdin.read()))
