from sys import stdin

# noinspection LongLine
samples = [
    (
        # Input 1
        """4\n1 2 3 4\n4 3 2 1\n2 2 2 2\n""",
        # Output 1
        """2 2 2 2\n"""
    ),
    (
        # Input 2
        """6\n3 1 4 1 5 9\n2 7 1 8 2 8\n1 6 1 8 0 3\n""",
        # Output 2
        """2 6 1 8 2 8\n"""
    ),
]


def solve(problem_input: str):
    lines = problem_input.splitlines()
    number_of_days = int(lines[0])
    out = ""
    prefs = []
    for person in lines[1::]:
        prefs.append([int(x) for x in person.split()])
    for day_number in range(number_of_days):
        options = []
        for person_prefs in prefs:
            options.append(person_prefs[day_number])
        out += f"{sorted(options)[1]} "
    return out.strip()


if __name__ == "__main__":
    print(solve(stdin.read()))
