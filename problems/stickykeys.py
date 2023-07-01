from sys import stdin

# noinspection LongLine
samples = [
    (
        # Input 1
        """UAAAAAPC\n""",
        # Output 1
        """UAPC\n"""
    ),
    (
        # Input 2
        """UUAAPPCCC is my 11th faavvorite conNtEest\n""",
        # Output 2
        """UAPC is my 1th favorite conNtEest\n"""
    ),
]


def solve(problem_input: str):
    problem_input = list(problem_input)
    for i, character in enumerate(problem_input):
        j = i + 1
        while j < len(problem_input) and character == problem_input[j]:
            del problem_input[j]
    return "".join(problem_input).strip()


if __name__ == "__main__":
    print(solve(stdin.read()))
