from sys import stdin

samples = [
    (
        # Input 1
        """3
3 0 2
""",
        # Output 1
        """1.6666666666666667
"""
    ),
    (
        # Input 2
        """3
1 -1 4
""",
        # Output 2
        """2.5
"""
    ),
    (
        # Input 3
        """11
-1 -1 -1 -1 0 0 0 0 0 0 1
""",
        # Output 3
        """0.14285714285714285
"""
    ),
]


def solve(problem_input: str):
    entries = problem_input.splitlines()[1].split()
    non_walks = [int(x) for x in entries if x != "-1"]
    return sum(non_walks) / len(non_walks)


if __name__ == "__main__":
    print(solve(stdin.read()))
