from sys import stdin

samples = [
    (
        # Sample Input 1
        """1
""",
        # Sample Output 1
        """first
"""
    ),
    (
        # Sample Input 2
        """2
""",
        # Sample Output 2
        """second
"""
    ),
    (
        # Sample Input 3
        """3
""",
        # Sample Output 3
        """first
"""
    ),
]


def solve(problem_input: str):
    if int(problem_input) & 1:  # means N is odd
        return "first"
    else:
        return "second"


if __name__ == "__main__":
    print(solve(stdin.read()))
