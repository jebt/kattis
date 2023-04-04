from sys import stdin

# noinspection LongLine
samples = [
    (
        # Input 1
        """2\n6 5.0000\n2 3.1222\n""",
        # Output 1
        """60.0000 72.0000 84.0000\n19.2172 38.4344 57.6517\n"""
    ),
]


def solve(problem_input: str):
    cases = problem_input.splitlines()[1::]
    out = ""
    for case in cases:
        b, p = case.split()
        b = int(b)
        p = float(p)
        min_abpm = (60 * (b - 1)) / p
        act_abpm = (60 * b) / p
        max_abpm = (60 * (b + 1)) / p
        out += f"{min_abpm:.4f} {act_abpm:.4f} {max_abpm:.4f}\n"
    return out.strip()


if __name__ == "__main__":
    print(solve(stdin.read()))
