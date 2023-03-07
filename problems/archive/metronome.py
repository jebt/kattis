from sys import stdin

samples = [
    (
        # Sample Input 1
        """16
""",
        # Sample Output 1
        """4.0
"""
    ),
    (
        # Sample Input 2
        """99
""",
        # Sample Output 2
        """24.75
"""
    ),
]


def solve(problem_input: str):
    return int(problem_input) / 4


if __name__ == "__main__":
    print(solve(stdin.read()))
