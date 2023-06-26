from sys import stdin

# noinspection LongLine
samples = [
    (
        # Input 1
        """3\nSkru op!\nSkru op!\nSkru ned!\n""",
        # Output 1
        """8\n"""
    ),
    (
        # Input 2
        """5\nSkru op!\nSkru op!\nSkru op!\nSkru op!\nSkru ned!\n""",
        # Output 2
        """9\n"""
    ),
]


def solve(problem_input: str):
    volume = 7
    requests = problem_input.splitlines()[1::]
    for request in requests:
        if "op" in request:
            if volume < 10:
                volume += 1
        elif volume > 0:
            volume -= 1
    return volume


if __name__ == "__main__":
    print(solve(stdin.read()))
