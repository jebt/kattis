from sys import stdin

samples = [
    (
        # Input 1
        """734 893
""",
        # Output 1
        """437
"""
    ),
    (
        # Input 2
        """221 231
""",
        # Output 2
        """132
"""
    ),
    (
        # Input 3
        """839 237
""",
        # Output 3
        """938
"""
    ),
]


def solve(problem_input: str):
    return max([int(n[2] + n[1] + n[0]) for n in problem_input.split()])


if __name__ == "__main__":
    print(solve(stdin.read()))
