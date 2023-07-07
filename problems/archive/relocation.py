from sys import stdin

# noinspection LongLine
samples = [
    (
        # Input 1
        """5 10\n5 2 8 1 4\n1 2 10\n2 4 5\n2 1 3\n1 4 3\n2 1 5\n2 5 2\n1 4 1\n2 2 4\n1 3 15\n2 4 1\n""",
        # Output 1
        """3\n3\n1\n6\n9\n4\n"""
    ),
]


def solve(problem_input: str):
    lines = problem_input.splitlines()
    # n, q = [int(x) for x in lines[0].split()]
    initial_locations = [int(x) for x in lines[1].split()]
    queries = lines[2::]
    companies = {}
    for i, initial_location in enumerate(initial_locations, 1):
        companies[i] = initial_location
    out = ""
    for query in queries:
        query_type, arg1, arg2 = [int(x) for x in query.split()]
        if query_type == 1:
            companies[arg1] = arg2
        else:
            out += f"{abs(companies[arg1] - companies[arg2])}\n"
    return out.strip()


if __name__ == "__main__":
    print(solve(stdin.read()))
