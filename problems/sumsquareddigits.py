import math
from sys import stdin

# noinspection LongLine
samples = [
    (
        # Input 1
        """3\n1 10 1234\n2 3 98765\n3 16 987654321\n""",
        # Output 1
        """1 30\n2 19\n3 696\n"""
    ),
]


def solve(problem_input: str):
    out = ""
    datasets = problem_input.splitlines()[1::]
    for dataset in datasets:
        i, b, n = [int(x) for x in dataset.split()]
        start_from_exponent = math.ceil(math.log(n, b))
        ssd = 0
        remaining = n
        for exponent in range(start_from_exponent, -1, -1):
            chunk = b**exponent
            times = remaining // chunk
            ssd += times**2
            remaining -= chunk * times
        out += f"{i} {ssd}\n"
    return out.strip()


if __name__ == "__main__":
    print(solve(stdin.read()))
