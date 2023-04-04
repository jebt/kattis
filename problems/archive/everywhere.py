from sys import stdin

# noinspection LongLine
samples = [
    (
        # Input 1
        """2\n7\nsaskatoon\ntoronto\nwinnipeg\ntoronto\nvancouver\nsaskatoon\ntoronto\n3\nedmonton\nedmonton\nedmonton\n""",
        # Output 1
        """4\n1\n"""
    ),
]


def solve(problem_input: str):
    lines = (line for line in problem_input.splitlines())
    next(lines)  # skip number of testcases
    out = ""
    while line := next(lines, None):
        number_of_cities = int(line)
        unique_cities = set()
        for i in range(number_of_cities):
            unique_cities.add(next(lines))
        out += f"{len(unique_cities)}\n"
    return out.strip()


if __name__ == "__main__":
    print(solve(stdin.read()))
