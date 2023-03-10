from sys import stdin

samples = [
    (
        # Input 1
        """80
""",
        # Output 1
        """1.2500000000
5.0000000000
"""
    ),
    (
        # Input 2
        """15
""",
        # Output 2
        """6.6666666667
1.1764705882
"""
    ),
]


def solve(problem_input: str):
    ratio1 = int(problem_input)/100
    ratio2 = 1 - ratio1
    return f"{1/ratio1:.10f}\n{1/ratio2:.10f}"


if __name__ == "__main__":
    print(solve(stdin.read()))
