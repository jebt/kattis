from sys import stdin

# noinspection LongLine
samples = [
    (
        # Input 1
        """2\n1 1\n""",
        # Output 1
        """2\n"""
    ),
    (
        # Input 2
        """5\n1 2 3 4 5\n""",
        # Output 2
        """15\n"""
    ),
]


def solve(problem_input: str):
    return sum([int(x) for x in problem_input.split()][1::])


if __name__ == "__main__":
    print(solve(stdin.read()))
