from sys import stdin

samples = [
    (
        # Input 1
        """3 4\n""",
        # Output 1
        """3 4\n"""
    ),
    (
        # Input 2
        """987 23\n""",
        # Output 2
        """23 987\n"""
    ),
]


def solve(problem_input: str):
    i1, i2 = sorted([int(x) for x in problem_input.split()])
    return f"{i1} {i2}"


if __name__ == "__main__":
    print(solve(stdin.read()))
