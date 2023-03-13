import itertools
from sys import stdin

samples = [
    (
        # Input 1
        """2\n3\n2 3\n4 5\n5 6\n""",
        # Output 1
        """112.0000000\n"""
    ),
    (
        # Input 2
        """0.75\n2\n2 3.333\n3.41 4.567\n""",
        # Output 2
        """16.6796025\n"""
    ),
]


def solve(problem_input: str):
    nums = [float(x) for x in problem_input.split()]
    cost_per_sqr = nums[0]
    total_cost = 0
    for length, width in zip(nums[2::2], nums[3::2]):
        total_cost += length * width * cost_per_sqr
    return f"{total_cost:.7f}"


if __name__ == "__main__":
    print(solve(stdin.read()))
