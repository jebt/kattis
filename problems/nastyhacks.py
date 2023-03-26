from sys import stdin

# noinspection LongLine
samples = [
    (
        # Input 1
        """3\n0 100 70\n100 130 30\n-100 -70 40\n""",
        # Output 1
        """advertise\ndoes not matter\ndo not advertise\n"""
    ),
]


def solve(problem_input: str):
    out = ""
    cases = problem_input.splitlines()[1::]
    for case in cases:
        without_ad, with_ad, cost = [int(x) for x in case.split()]
        gain = with_ad - without_ad
        if gain == cost:
            out += "does not matter\n"
        elif gain > cost:
            out += "advertise\n"
        else:
            out += "do not advertise\n"
    return out.strip()


if __name__ == "__main__":
    print(solve(stdin.read()))
