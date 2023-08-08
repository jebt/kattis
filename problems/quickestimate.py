from sys import stdin

# noinspection LongLine
samples = [
    (
        # Input 1
        """\n5\n314\n1\n5926\n5\n35897\n""",
        # Output 1
        """\n3\n1\n4\n1\n5\n"""
    ),
    (
        # Input 2
        """\n3\n0\n10\n100\n""",
        # Output 2
        """\n1\n2\n3\n"""
    ),
]


def solve(problem_input: str):
    # out = []
    # for case in problem_input.strip().splitlines()[1:]:
    #     out.append(str(len(case)))
    # return "\n".join(out)

    out = ""
    for case in problem_input.strip().splitlines()[1::]:
        out += f"{len(case)}\n"
    return out.strip()


if __name__ == "__main__":
    print(solve(stdin.read()))
