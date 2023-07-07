from sys import stdin

# noinspection LongLine
samples = [
    (
        # Input 1
        """13\n""",
        # Output 1
        """11\n"""
    ),
    (
        # Input 2
        """47\n""",
        # Output 2
        """61\n"""
    ),
]


def solve(problem_input: str):
    number = int(problem_input)
    reversed_bin_num = bin(number)[:1:-1]
    return int(reversed_bin_num, 2)


if __name__ == "__main__":
    print(solve(stdin.read()))
