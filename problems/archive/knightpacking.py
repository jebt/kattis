from sys import stdin

samples = [
    (
        # Sample Input 1
        """1
""".strip(),
        # Sample Output 1
        """first
""".strip()
    ),
    (
        # Sample Input 2
        """2
""".strip(),
        # Sample Output 2
        """second
""".strip()
    ),
    (
        # Sample Input 3
        """3
""".strip(),
        # Sample Output 3
        """first
""".strip()
    ),
]


def solve(problem_input: str):
    if int(problem_input) & 1:  # means N is odd
        return "first"
    else:
        return "second"


if __name__ == "__main__":
    print(solve(stdin.read()))
