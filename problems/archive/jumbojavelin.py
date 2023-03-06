from sys import stdin

samples = [
    (
        # Sample Input 1
        """4
21
34
18
9
""".strip(),
        # Sample Output 1
        """79
""".strip()
    ),
    (
        # Sample Input 2
        """3
1
50
40
""".strip(),
        # Sample Output 2
        """89
""".strip()
    ),
]


def solve(problem_input: str):
    ints = (int(x) for x in problem_input.splitlines())
    count = next(ints)
    return sum(ints) - (count - 1)


if __name__ == "__main__":
    print(solve(stdin.read()))
