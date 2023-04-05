from sys import stdin

# noinspection LongLine
samples = [
    (
        # Input 1
        """1\n100\n4\n""",
        # Output 1
        """4\n40\n"""
    ),
    (
        # Input 2
        """100\n500\n12\n""",
        # Output 2
        """129\n480\n"""
    ),
    (
        # Input 3
        """1\n10000\n1\n""",
        # Output 3
        """1\n10000\n"""
    ),
]


def solve(problem_input: str):
    minimum_n, maximum_m, target_of_sum = [int(x) for x in problem_input.split()]
    n, m = None, None
    while not n:
        if sum_of_digits(minimum_n) == target_of_sum:
            n = minimum_n
        minimum_n += 1
    while not m:
        if sum_of_digits(maximum_m) == target_of_sum:
            m = maximum_m
        maximum_m -= 1
    return f"{n}\n{m}"


def sum_of_digits(n):
    return sum(int(x) for x in str(n))


if __name__ == "__main__":
    print(solve(stdin.read()))
