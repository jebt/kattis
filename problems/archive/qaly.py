from sys import stdin

samples = [
    (
        # Sample Input 1
        """5
1.0 12.0
0.7 5.2
0.9 10.7
0.5 20.4
0.2 30.0
""",
        # Sample Output 1
        """41.470
"""
    ),
]


def solve(problem_input: str):
    answer = 0.0
    for line in problem_input.splitlines()[1::]:
        parts = line.split()
        answer += float(parts[0]) * float(parts[1])
    return f"{answer:.3f}"


if __name__ == "__main__":
    print(solve(stdin.read()))
