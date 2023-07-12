from sys import stdin

# noinspection LongLine
samples = [
    (
        # Input 1
        """1 2 3 4\n""",
        # Output 1
        """3\n"""
    ),
    (
        # Input 2
        """4 4 3 4\n""",
        # Output 2
        """12\n"""
    ),
]


def solve(problem_input: str):
    nums = sorted([int(x) for x in problem_input.split()])
    return nums[0] * nums[2]


if __name__ == "__main__":
    print(solve(stdin.read()))
