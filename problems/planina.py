from sys import stdin

samples = [
    (
        # Input 1
        """1\n""",
        # Output 1
        """9\n"""
    ),
    (
        # Input 2
        """2\n""",
        # Output 2
        """25\n"""
    ),
    (
        # Input 3
        """5\n""",
        # Output 3
        """1089\n"""
    ),
]


def solve(problem_input: str):
    iteration = int(problem_input)
    return points(iteration)


def points(iteration):
    return (4 ** iteration) + (2 * (2 ** iteration)) + 1


if __name__ == "__main__":
    print(solve(stdin.read()))
