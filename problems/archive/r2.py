from sys import stdin

samples = [
    (
        # Sample Input 1
        """11 15
""",
        # Sample Output 1
        """19
"""
    ),
    (
        # Sample Input 2
        """4 3
""",
        # Sample Output 2
        """2
"""
    ),
]


def solve(problem_input: str):
    ints = [int(x) for x in problem_input.split()]
    return ints[1] + ints[1] - ints[0]


if __name__ == "__main__":
    print(solve(stdin.read()))
