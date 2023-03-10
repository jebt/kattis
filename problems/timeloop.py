from sys import stdin

samples = [
    (
        # Input 1
        """5\n""",
        # Output 1
        """1 Abracadabra\n2 Abracadabra\n3 Abracadabra\n4 Abracadabra\n5 Abracadabra\n"""
    ),
    (
        # Input 2
        """10\n""",
        # Output 2
        """1 Abracadabra\n2 Abracadabra\n3 Abracadabra\n4 Abracadabra\n5 Abracadabra\n6 Abracadabra\n7 Abracadabra\n8 Abracadabra\n9 Abracadabra\n10 Abracadabra\n"""  # noqa
    ),
]


def solve(problem_input: str):
    out = ""
    for i in range(int(problem_input)):
        out += f"{i + 1} Abracadabra\n"
    return out.strip()


if __name__ == "__main__":
    print(solve(stdin.read()))
