from sys import stdin

samples = [
    (
        # Input 1
        """1 19\n""",
        # Output 1
        """0\n"""
    ),
    (
        # Input 2
        """4 4\n""",
        # Output 2
        """0\n"""
    ),
    (
        # Input 3
        """23 14\n""",
        # Output 3
        """1\n"""
    ),
]


def solve(problem_input: str):
    ints = [int(x) for x in problem_input.split()]
    return 1 if ints[0] > ints[1] else 0


if __name__ == "__main__":
    print(solve(stdin.read()))
