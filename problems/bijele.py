from sys import stdin

# noinspection LongLine
samples = [
    (
        # Input 1
        """0 1 2 2 2 7\n""",
        # Output 1
        """1 0 0 0 0 1\n"""
    ),
    (
        # Input 2
        """2 1 2 1 2 1\n""",
        # Output 2
        """-1 0 0 1 0 7\n"""
    ),
]


def solve(problem_input: str):
    needed = [1, 1, 2, 2, 2, 8]
    got = [int(x) for x in problem_input.split()]
    change = [n - g for n, g in zip(needed, got)]
    return " ".join(str(x) for x in change)


if __name__ == "__main__":
    print(solve(stdin.read()))
