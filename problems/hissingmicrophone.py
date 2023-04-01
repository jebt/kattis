from sys import stdin

# noinspection LongLine
samples = [
    (
        # Input 1
        """amiss\n""",
        # Output 1
        """hiss\n"""
    ),
    (
        # Input 2
        """octopuses\n""",
        # Output 2
        """no hiss\n"""
    ),
    (
        # Input 3
        """hiss\n""",
        # Output 3
        """hiss\n"""
    ),
]


def solve(problem_input: str):
    word = problem_input.strip()
    last_was_s = False
    for letter in word:
        if letter == "s":
            if last_was_s:
                return "hiss"
            else:
                last_was_s = True
        else:
            last_was_s = False
    return "no hiss"


if __name__ == "__main__":
    print(solve(stdin.read()))
