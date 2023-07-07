from sys import stdin

# noinspection LongLine
samples = [
    (
        # Input 1
        """30 30 27 27\n""",
        # Output 1
        """1\n"""
    ),
    (
        # Input 2
        """35 30 25 29\n""",
        # Output 2
        """0\n"""
    ),
    (
        # Input 3
        """30 35 30 35\n""",
        # Output 3
        """0\n"""
    ),
]


def solve(problem_input: str):
    wc, hc, ws, hs = [int(x) for x in problem_input.split()]
    return int(wc - ws >= 2 and hc - hs >= 2)


if __name__ == "__main__":
    print(solve(stdin.read()))
