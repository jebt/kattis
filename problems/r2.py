from sys import stdin

title = "R2"
problem_id = "r2"
sample_input_1 = """11 15
""".strip()
sample_input_2 = """4 3
""".strip()
sample_output_1 = """19
""".strip()
sample_output_2 = """2
""".strip()


def solve(problem_input: str):
    ints = [int(x) for x in problem_input.split()]
    return ints[1] + ints[1] - ints[0]


if __name__ == "__main__":
    print(solve(stdin.read()))
