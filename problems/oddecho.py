from sys import stdin

samples = [
    (
        # Sample Input 1
        """5
hello
i
am
an
echo
""".strip(),
        # Sample Output 1
        """hello
am
echo
""".strip()
    ),
    (
        # Sample Input 2
        """10
only
if
these
oddindexed
words
appear
are
you
correct
output
""".strip(),
        # Sample Output 2
        """only
these
words
are
correct
""".strip()
    ),
]


def solve(problem_input: str):
    return "\n".join(problem_input.splitlines()[1::2])


if __name__ == "__main__":
    print(solve(stdin.read()))
