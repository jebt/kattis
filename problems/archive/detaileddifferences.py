from sys import stdin

# noinspection LongLine
samples = [
    (
        # Input 1
        """3\nATCCGCTTAGAGGGATT\nGTCCGTTTAGAAGGTTT\nabcdefghijklmnopqrstuvwxyz\nbcdefghijklmnopqrstuvwxyza\nabcdefghijklmnopqrstuvwxyz0123456789\nabcdefghijklmnopqrstuvwxyz0123456789\n""",
        # Output 1
        """ATCCGCTTAGAGGGATT\nGTCCGTTTAGAAGGTTT\n*....*.....*..*..\n\nabcdefghijklmnopqrstuvwxyz\nbcdefghijklmnopqrstuvwxyza\n**************************\n\nabcdefghijklmnopqrstuvwxyz0123456789\nabcdefghijklmnopqrstuvwxyz0123456789\n....................................\n\n"""
    ),
]


def solve(problem_input: str):
    out = ""
    lines = (line for line in problem_input.splitlines())
    next(lines)  # skip number of testcases
    while line_a := next(lines, None):
        line_b = next(lines)
        line_c = ""
        for char_a, char_b in zip(line_a, line_b):
            if char_a == char_b:
                line_c += "."
            else:
                line_c += "*"
        line_c += "\n\n"
        out += f"{line_a}\n{line_b}\n{line_c}"
    return out.strip()


if __name__ == "__main__":
    print(solve(stdin.read()))
