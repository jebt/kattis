from sys import stdin

samples = [
    (
        # Input 1
        """robust\n""",
        # Output 1
        """1\n"""
    ),
    (
        # Input 2
        """icpc\n""",
        # Output 2
        """0\n"""
    ),
]


def solve(problem_input: str):
    return 1 if len(problem_input) == len(set(problem_input)) else 0


if __name__ == "__main__":
    print(solve(stdin.read()))
