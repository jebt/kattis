from sys import stdin

samples = [
    (
        # Input 1
        """Hello
""",
        # Output 1
        """Hello Hello Hello
"""
    ),
    (
        # Input 2
        """ECHO
""",
        # Output 2
        """ECHO ECHO ECHO
"""
    ),
]


def solve(problem_input: str):
    word = problem_input.strip()
    return f"{word} {word} {word}"


if __name__ == "__main__":
    print(solve(stdin.read()))
