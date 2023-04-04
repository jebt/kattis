from sys import stdin

# noinspection LongLine
samples = [
    (
        # Input 1
        """3\n3 2 3 4\n10 4 4 4 4 4 4 4 4 4 4\n4 10 10 10 10\n""",
        # Output 1
        """7\n31\n37\n"""
    ),
]


def solve(problem_input: str):
    cases = problem_input.splitlines()[1::]
    out = ""
    for case in cases:
        strips = [int(x) for x in case.split()[1::]]
        outlets = 1 + sum(strips) - len(strips)
        out += f"{outlets}\n"
    return out.strip()


if __name__ == "__main__":
    print(solve(stdin.read()))
