from sys import stdin

samples = [
    (
        # Input 1
        """4\n7\n2 3\n1 4\n1 2\n1 2\n2 2\n2 2\n2 1\n""",
        # Output 1
        """6\n"""
    ),
]


def solve(problem_input: str):
    pieces = problem_input.splitlines()[2:]
    total_area = 0
    for piece in pieces:
        l, w = [int(x) for x in piece.split()]
        total_area += l * w
    return total_area // int(problem_input.split()[0])


if __name__ == "__main__":
    print(solve(stdin.read()))
