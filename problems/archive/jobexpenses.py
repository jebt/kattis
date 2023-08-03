from sys import stdin

# noinspection LongLine
samples = [
    (
        # Input 1
        """3\n1 -2 3\n""",
        # Output 1
        """2\n"""
    ),
    (
        # Input 2
        """5\n129 44 394 253 147\n""",
        # Output 2
        """0\n"""
    ),
    (
        # Input 3
        """10\n-100 40000 -6500 -230 -18 34500 -450 13000 -100 5000\n""",
        # Output 3
        """7398\n"""
    ),
]


def solve(problem_input: str):
    return abs(sum([int(x) for x in problem_input.split() if x[0] == "-"]))


if __name__ == "__main__":
    print(solve(stdin.read()))
