from sys import stdin

# noinspection LongLine
samples = [
    (
        # Input 1
        """5\n1\n2\n3\n4\n5\n""",
        # Output 1
        """5\n4\n3\n2\n1\n"""
    ),
    (
        # Input 2
        """3\n10\n12\n9\n""",
        # Output 2
        """9\n12\n10\n"""
    ),
]


def solve(problem_input: str):
    # numbers = problem_input.splitlines()[1::]
    # out = ""
    # for number in reversed(numbers):
    #     out += f"{number}\n"
    # return out.strip()

    return "\n".join(problem_input.splitlines()[:0:-1])


if __name__ == "__main__":
    print(solve(stdin.read()))
