from sys import stdin

# noinspection LongLine
samples = [
    (
        # Input 1
        """OCT 31\n""",
        # Output 1
        """yup\n"""
    ),
    (
        # Input 2
        """JUN 24\n""",
        # Output 2
        """nope\n"""
    ),
]


def solve(problem_input: str):
    if problem_input.strip() == "OCT 31" or problem_input.strip() == "DEC 25":
        return "yup"
    else:
        return "nope"


if __name__ == "__main__":
    print(solve(stdin.read()))
