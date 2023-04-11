from sys import stdin

# noinspection LongLine
samples = [
    (
        # Input 1
        """5 5\n5 7\n7 5\n""",
        # Output 1
        """7 7\n"""
    ),
    (
        # Input 2
        """30 20\n10 10\n10 20\n""",
        # Output 2
        """30 10\n"""
    ),
]


def solve(problem_input: str):
    xs, ys = [], []
    for line in problem_input.splitlines():
        parts = line.split()
        xs.append(int(parts[0]))
        ys.append(int(parts[1]))

    unique_x = list(set(xs))
    unique_y = list(set(ys))

    if xs.count(unique_x[0]) == 1:
        x = unique_x[0]
    else:
        x = unique_x[1]

    if ys.count(unique_y[0]) == 1:
        y = unique_y[0]
    else:
        y = unique_y[1]

    return f"{x} {y}"


if __name__ == "__main__":
    print(solve(stdin.read()))
