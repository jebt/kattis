from sys import stdin

# noinspection LongLine
samples = [
    (
        # Input 1
        """ahjmnoy\nacijjkll\n""",
        # Output 1
        """aachijjjkllmnoy\n"""
    ),
]


def solve(problem_input: str):
    lines = problem_input.splitlines()
    letters = lines[0]+lines[1]
    return "".join(sorted(letters))


if __name__ == "__main__":
    print(solve(stdin.read()))
