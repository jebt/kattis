from sys import stdin

samples = [
    (
        # Input 1
        """12000 3000 5\n400 25 200 80 500\n""",
        # Output 1
        """6895\n"""
    ),
    (
        # Input 2
        """10000 4000 7\n110 10 20 10 5 3 5\n""",
        # Output 2
        """5237\n"""
    ),
]


def solve(problem_input: str):
    g, t, n, *items = [int(x) for x in problem_input.split()]
    towing_capacity = (g - t) * 0.9
    return int(towing_capacity) - sum(items)


if __name__ == "__main__":
    print(solve(stdin.read()))
