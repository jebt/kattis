from sys import stdin

# noinspection LongLine
samples = [
    (
        # Input 1
        """THE RAIN IN SPAIN\n""",
        # Output 1
        """yes\n"""
    ),
    (
        # Input 2
        """IN THE RAIN AND THE SNOW\n""",
        # Output 2
        """no\n"""
    ),
    (
        # Input 3
        """THE RAIN IN SPAIN IN THE PLAIN\n""",
        # Output 3
        """no\n"""
    ),
]


def solve(problem_input: str):
    words = problem_input.split()
    for word in words:
        if words.count(word) > 1:
            return "no"
    return "yes"


if __name__ == "__main__":
    print(solve(stdin.read()))
