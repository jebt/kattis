from sys import stdin

# noinspection LongLine
samples = [
    (
        # Input 1
        """3\n10\n9\n-5\n""",
        # Output 1
        """10 is even\n9 is odd\n-5 is odd\n"""
    ),
]


def solve(problem_input: str):
    ints = problem_input.split()[1:]
    out = ""
    for n in ints:
        out += f"{n} is odd\n" if int(n) & 1 else f"{n} is even\n"
        # out += f"{n} is odd\n" if int(n) % 2 == 1 else f"{n} is even\n"
    return out.strip()


if __name__ == "__main__":
    print(solve(stdin.read()))
