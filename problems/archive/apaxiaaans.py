from sys import stdin

samples = [
    (
        # Input 1
        """robert\n""",
        # Output 1
        """robert\n"""
    ),
    (
        # Input 2
        """rooobert\n""",
        # Output 2
        """robert\n"""
    ),
    (
        # Input 3
        """roooooobertapalaxxxxios\n""",
        # Output 3
        """robertapalaxios\n"""
    ),
]


def solve(problem_input: str):
    name = list(problem_input.strip())
    while True:
        for i, char in enumerate(name[:-1]):
            if char == name[i + 1]:
                name = name[:i] + name[i + 1:]
                break
        else:  # no break
            break
    return "".join(name)


if __name__ == "__main__":
    print(solve(stdin.read()))
