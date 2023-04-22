from sys import stdin

# noinspection LongLine
samples = [
    (
        # Input 1
        """N-FBI1\n9A-USKOK\nI-NTERPOL\nG-MI6\nRF-KGB1\n""",
        # Output 1
        """1\n"""
    ),
    (
        # Input 2
        """N321-CIA\nF3-B12I\nF-BI-12\nOVO-JE-CIA\nKRIJUMCAR1\n""",
        # Output 2
        """HE GOT AWAY!\n"""
    ),
    (
        # Input 3
        """47-FBI\nBOND-007\nRF-FBI18\nMARICA-13\n13A-FBILL\n""",
        # Output 3
        """1 3 5\n"""
    ),
]


def solve(problem_input: str):
    out = ""
    for i, line in enumerate(problem_input.splitlines()):
        if "FBI" in line:
            out += f"{i + 1} "
    if out == "":
        out = "HE GOT AWAY!"
    return out.strip()


if __name__ == "__main__":
    print(solve(stdin.read()))
