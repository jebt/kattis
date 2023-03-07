from sys import stdin

samples = [
    (
        # Input 1
        """3 4 5
""",
        # Output 1
        """60
"""
    ),
    (
        # Input 2
        """2 2 2
""",
        # Output 2
        """8
"""
    ),
    (
        # Input 3
        """3 1 5
""",
        # Output 3
        """15
"""
    ),
]


def solve(problem_input: str):
    # return reduce(mul, [int(x) for x in problem_input.split()])
    number = 1
    for x in [int(x) for x in problem_input.split()]:
        number *= x
    return number


if __name__ == "__main__":
    print(solve(stdin.read()))
