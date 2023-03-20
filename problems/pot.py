from sys import stdin

samples = [
    (
        # Input 1
        """2\n212\n1253\n""",
        # Output 1
        """1953566\n"""
    ),
    (
        # Input 2
        """5\n23\n17\n43\n52\n22\n""",
        # Output 2
        """102\n"""
    ),
    (
        # Input 3
        """3\n213\n102\n45\n""",
        # Output 3
        """10385\n"""
    ),
]


def solve(problem_input: str):
    numbers = problem_input.split()[1:]
    outcome = 0
    for number in numbers:
        base = int(number[:-1])
        exponent = int(number[-1])
        outcome += base**exponent
    return outcome


if __name__ == "__main__":
    print(solve(stdin.read()))
