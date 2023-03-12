from sys import stdin

samples = [
    (
        # Input 1
        """2 1\ncarrots?\nbunnies\n""",
        # Output 1
        """1\n"""
    ),
    (
        # Input 2
        """1 5\nsovl problmz\n""",
        # Output 2
        """5\n"""
    ),
]


def solve(problem_input: str):
    return problem_input.split()[1]


if __name__ == "__main__":
    print(solve(stdin.read()))
