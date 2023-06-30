from sys import stdin

# noinspection LongLine
samples = [
    (
        # Input 1
        """2 3 5\n""",
        # Output 1
        """correct!\n"""
    ),
    (
        # Input 2
        """1 1 3\n""",
        # Output 2
        """wrong!\n"""
    ),
    (
        # Input 3
        """-1 1 0\n""",
        # Output 3
        """correct!\n"""
    ),
]


def solve(problem_input: str):
    nums = [int(x) for x in problem_input.split()]
    return "correct!" if nums[0] + nums[1] == nums[2] else "wrong!"


if __name__ == "__main__":
    print(solve(stdin.read()))
