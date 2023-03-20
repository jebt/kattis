from sys import stdin

samples = [
    (
        # Input 1
        """10\n3\n4\n6\n2\n""",
        # Output 1
        """28\n"""
    ),
    (
        # Input 2
        """10\n3\n10\n2\n12\n""",
        # Output 2
        """16\n"""
    ),
    (
        # Input 3
        """15\n3\n15\n10\n20\n""",
        # Output 3
        """15\n"""
    ),
]


def solve(problem_input: str):
    ints = [int(x) for x in problem_input.split()]
    mb_per_month = ints[0]
    months_so_far = ints[1]
    mb_used = sum(ints[2:])
    return (mb_per_month * (months_so_far + 1)) - mb_used


if __name__ == "__main__":
    print(solve(stdin.read()))
