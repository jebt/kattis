from sys import stdin

# noinspection LongLine
samples = [
    (
        # Input 1
        """\nTCGTTC\n""",
        # Output 1
        """\n21\n"""
    ),
    (
        # Input 2
        """\nCCC\n""",
        # Output 2
        """\n9\n"""
    ),
    (
        # Input 3
        """\nTTCCGG\n""",
        # Output 3
        """\n26\n"""
    ),
]


def solve(problem_input: str):
    # counts = sorted([problem_input.count("T"), problem_input.count("C"), problem_input.count("G")])

    # counts = []
    # for ssc in "TCG":
    #     counts.append(problem_input.count(ssc))
    # counts.sort()

    counts = sorted([problem_input.count(c) for c in "TCG"])

    # points = 0
    # for count in counts:
    #     points += count ** 2

    points = sum(x ** 2 for x in counts)

    return points + 7 * counts[0]


if __name__ == "__main__":
    print(solve(stdin.read()))
