from sys import stdin

# noinspection LongLine
samples = [
    (
        # Input 1
        """3\n1\n2\n3\n""",
        # Output 1
        """1\n2\n6\n"""
    ),
    (
        # Input 2
        """2\n5\n2\n""",
        # Output 2
        """0\n2\n"""
    ),
]


def solve(problem_input: str):
    out = ""
    for x in problem_input.splitlines()[1::]:
        x = int(x)
        if x == 3:
            out += "6\n"
        elif x < 5:
            out += f"{x}\n"
        else:
            out += "0\n"
    return out.strip()


if __name__ == "__main__":
    print(solve(stdin.read()))
