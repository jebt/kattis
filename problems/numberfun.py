from sys import stdin

# noinspection LongLine
samples = [
    (
        # Input 1
        """6\n1 2 3\n2 24 12\n5 3 1\n9 16 7\n7 2 14\n12 4 2\n""",
        # Output 1
        """Possible\nPossible\nImpossible\nPossible\nPossible\nImpossible\n"""
    ),
]


def solve(problem_input: str):
    cases = problem_input.splitlines()[1::]
    out = ""
    for case in cases:
        a, b, c = [int(x) for x in case.split()]
        if a + b == c or a - b == c or b - a == c or a * b == c or a / b == c or b / a == c:
            out += "Possible\n"
        else:
            out += "Impossible\n"
    return out.strip()


if __name__ == "__main__":
    print(solve(stdin.read()))
