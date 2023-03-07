from sys import stdin

samples = [
    (
        # Input 1
        """hey
""",
        # Output 1
        """heey
"""
    ),
    (
        # Input 2
        """heeeeey
""",
        # Output 2
        """heeeeeeeeeey
"""
    ),
]


def solve(problem_input: str):
    return "h" + "e" * (len(problem_input.strip()) - 2) * 2 + "y"


if __name__ == "__main__":
    print(solve(stdin.read()))
