from sys import stdin

# noinspection LongLine
samples = [
    (
        # Input 1
        """6 6\n""",
        # Output 1
        """7\n"""
    ),
    (
        # Input 2
        """6 4\n""",
        # Output 2
        """5\n6\n7\n"""
    ),
    (
        # Input 3
        """12 20\n""",
        # Output 3
        """13\n14\n15\n16\n17\n18\n19\n20\n21\n"""
    ),
]


def solve(problem_input: str):
    die = sorted([int(x) for x in problem_input.split()])
    out = ""
    for i in range(die[0] + 1, die[1] + 2):
        out += f"{i}\n"
    return out.strip()


if __name__ == "__main__":
    print(solve(stdin.read()))
