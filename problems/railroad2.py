from sys import stdin

# noinspection LongLine
samples = [
    (
        # Input 1
        """1 0\n""",
        # Output 1
        """possible\n"""
    ),
    (
        # Input 2
        """0 2\n""",
        # Output 2
        """possible\n"""
    ),
    (
        # Input 3
        """1 3\n""",
        # Output 3
        """impossible\n"""
    ),
]


def solve(problem_input: str):
    y = int(problem_input.split()[1])
    return "possible" if y % 2 == 0 else "impossible"


if __name__ == "__main__":
    print(solve(stdin.read()))
