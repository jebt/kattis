from sys import stdin

# noinspection LongLine
samples = [
    (
        # Input 1
        """10 4 7\n""",
        # Output 1
        """168\n"""
    ),
    (
        # Input 2
        """5 2 2\n""",
        # Output 2
        """36\n"""
    ),
    (
        # Input 3
        """4 2 1\n""",
        # Output 3
        """24\n"""
    ),
]


def solve(problem_input: str):
    nums = [int(x) for x in problem_input.split()]
    length = max([nums[1], nums[0] - nums[1]])
    width = max([nums[2], nums[0] - nums[2]])
    return length * width * 4


if __name__ == "__main__":
    print(solve(stdin.read()))
