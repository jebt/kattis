from sys import stdin

samples = [
    (
        # Input 1
        """1 1\n""",
        # Output 1
        """2\n"""
    ),
    (
        # Input 2
        """2 2\n""",
        # Output 2
        """4\n"""
    ),
]


def solve(problem_input: str):
    return sum(int(x) for x in problem_input.split())


if __name__ == "__main__":
    print(solve(stdin.read()))
