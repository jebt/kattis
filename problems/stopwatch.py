from sys import stdin

samples = [
    (
        # Input 1
        """2\n7\n11\n""",
        # Output 1
        """4\n"""
    ),
    (
        # Input 2
        """5\n2\n5\n9\n10\n17\n""",
        # Output 2
        """still running\n"""
    ),
    (
        # Input 3
        """4\n0\n2\n104\n117\n""",
        # Output 3
        """15\n"""
    ),
]


def solve(problem_input: str):
    ints = [int(x) for x in problem_input.split()]
    if ints[0] & 1:
        return "still running"
    counter = 0
    for i, stop in enumerate(ints[2::2]):
        counter += (stop - ints[(i * 2) + 1])
    return counter


if __name__ == "__main__":
    print(solve(stdin.read()))
