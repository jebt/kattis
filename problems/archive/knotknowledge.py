from sys import stdin

# noinspection LongLine
samples = [
    (
        # Input 1
        """4\n1 2 4 3\n4 2 3\n""",
        # Output 1
        """1\n"""
    ),
    (
        # Input 2
        """4\n10 101 999 1\n1 999 101\n""",
        # Output 2
        """10\n"""
    ),
]


def solve(problem_input: str):
    lines = problem_input.splitlines()
    needs_to_learn = set([int(x) for x in lines[1].split()])
    learned = set([int(x) for x in lines[2].split()])
    missed = needs_to_learn.difference(learned)
    missed_element, = missed
    return missed_element


if __name__ == "__main__":
    print(solve(stdin.read()))
