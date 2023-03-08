from sys import stdin

samples = [
    (
        # Input 1
        """5551212
""",
        # Output 1
        """1
"""
    ),
    (
        # Input 2
        """5519876
""",
        # Output 2
        """0
"""
    ),
    (
        # Input 3
        """5055555
""",
        # Output 3
        """0
"""
    ),
    (
        # Input 4
        """5550000
""",
        # Output 4
        """1
"""
    ),
]


def solve(problem_input: str):
    return 1 if problem_input[:3] == "555" else 0


if __name__ == "__main__":
    print(solve(stdin.read()))
