from sys import stdin

# noinspection LongLine
samples = [
    (
        # Input 1
        """AB\n""",
        # Output 1
        """3\n"""
    ),
    (
        # Input 2
        """CBABCACCC\n""",
        # Output 2
        """1\n"""
    ),
]


def solve(problem_input: str):
    loc = 1
    for move in problem_input:
        if move == "A":
            if loc == 1:
                loc = 2
            elif loc == 2:
                loc = 1
        elif move == "B":
            if loc == 2:
                loc = 3
            elif loc == 3:
                loc = 2
        elif move == "C":
            if loc == 1:
                loc = 3
            elif loc == 3:
                loc = 1
    return loc


if __name__ == "__main__":
    print(solve(stdin.read()))
