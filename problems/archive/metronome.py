from sys import stdin

samples = [
    (
        # Sample Input 1
        """16
""".strip(),
        # Sample Output 1
        """4.0
""".strip()
    ),
    (
        # Sample Input 2
        """99
""".strip(),
        # Sample Output 2
        """24.75
""".strip()
    ),
]


def solve(problem_input: str):
    return int(problem_input) / 4


if __name__ == "__main__":
    print(solve(stdin.read()))
