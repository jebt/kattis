from sys import stdin

# noinspection LongLine
samples = [
    (
        # Input 1
        """|()||\n""",
        # Output 1
        """fix\n"""
    ),
    (
        # Input 2
        """||||()||||\n""",
        # Output 2
        """correct\n"""
    ),
    (
        # Input 3
        """|()|\n""",
        # Output 3
        """correct\n"""
    ),
    (
        # Input 4
        """|||()|\n""",
        # Output 4
        """fix\n"""
    ),
]


def solve(problem_input: str):
    sides = problem_input.strip().split("()")
    if len(sides[0]) == len(sides[1]):
        return "correct"
    else:
        return "fix"


if __name__ == "__main__":
    print(solve(stdin.read()))
