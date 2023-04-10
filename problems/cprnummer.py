from sys import stdin

# noinspection LongLine
samples = [
    (
        # Input 1
        """070761-4285\n""",
        # Output 1
        """1\n"""
    ),
    (
        # Input 2
        """051002-4321\n""",
        # Output 2
        """0\n"""
    ),
    (
        # Input 3
        """310111-0469\n""",
        # Output 3
        """1\n"""
    ),
]


def solve(problem_input: str):
    # return 1 if sum(factor * int(digit) for factor, digit in zip([4, 3, 2, 7, 6, 5, 4, 3, 2, 1], problem_input.replace("-", ""))) % 11 == 0 else 0  # noqa
    multipliers = [4, 3, 2, 7, 6, 5, 4, 3, 2, 1]
    cpr = problem_input.replace("-", "")
    total = sum(factor * int(digit) for factor, digit in zip(multipliers, cpr))
    return 1 if total % 11 == 0 else 0


if __name__ == "__main__":
    print(solve(stdin.read()))
