from sys import stdin

samples = [
    (
        # Input 1
        """banana
""",
        # Output 1
        """anana
"""
    ),
    (
        # Input 2
        """polarbear
""",
        # Output 2
        """arbear
"""
    ),
    (
        # Input 3
        """art
""",
        # Output 3
        """art
"""
    ),
]


def solve(problem_input: str):
    i = problem_input.index("a")
    return problem_input[i:].strip()


if __name__ == "__main__":
    print(solve(stdin.read()))
