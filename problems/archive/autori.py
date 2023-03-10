from sys import stdin

samples = [
    (
        # Input 1
        """Knuth-Morris-Pratt\n""",
        # Output 1
        """KMP\n"""
    ),
    (
        # Input 2
        """Mirko-Slavko\n""",
        # Output 2
        """MS\n"""
    ),
    (
        # Input 3
        """Pasko-Patak\n""",
        # Output 3
        """PP\n"""
    ),
]


def solve(problem_input: str):
    parts = problem_input.split("-")
    out = ""
    for part in parts:
        out += part[0]
    return out


if __name__ == "__main__":
    print(solve(stdin.read()))
