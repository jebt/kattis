from sys import stdin

samples = [
    (
        # Input 1
        """3\n1 8\n2 1\n3 10\n""",
        # Output 1
        """1 44\n2 2\n3 65\n"""
    ),
]


def solve(problem_input: str):
    datasets = problem_input.splitlines()[1::]
    out = ""
    for dataset in datasets:
        set_no, days = dataset.split()
        out += set_no
        candles = 0
        for day in range(int(days)):
            candles += day + 2
        out += f" {candles}\n"
    return out.strip()


if __name__ == "__main__":
    print(solve(stdin.read()))
