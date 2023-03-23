from sys import stdin

samples = [
    (
        # Input 1
        """3 4\n""",
        # Output 1
        """7\n"""
    ),
    (
        # Input 2
        """987 23\n""",
        # Output 2
        """1010\n"""
    ),
]


def solve(problem_input: str):
    return sum(int(x) for x in problem_input.split())


if __name__ == "__main__":
    print(solve(stdin.read()))
