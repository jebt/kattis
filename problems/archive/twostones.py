from sys import stdin

samples = [
    (
        # Input 1
        """1\n""",
        # Output 1
        """Alice\n"""
    ),
    (
        # Input 2
        """2\n""",
        # Output 2
        """Bob\n"""
    ),
    (
        # Input 3
        """5\n""",
        # Output 3
        """Alice\n"""
    ),
]


def solve(problem_input: str):
    is_odd = int(problem_input) & 1
    return "Alice" if is_odd else "Bob"


if __name__ == "__main__":
    print(solve(stdin.read()))
