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
        ssd = 0

        # start_from_exponent = math.ceil(math.log(n, b))
        # for exponent in range(start_from_exponent, -1, -1):
        #     chunk = b**exponent
        #     times = n // chunk
        #     ssd += times**2
        #     n -= chunk * times

        exponent = 0
        while n > 0:
            residue = n % b ** (exponent + 1)
            ssd += (residue // b ** exponent) ** 2
            n -= residue
            exponent += 1

        out += f"{i} {ssd}\n"
    return out.strip()








if __name__ == "__main__":
    print(solve(stdin.read()))
