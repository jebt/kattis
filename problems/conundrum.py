from sys import stdin

# noinspection LongLine
samples = [
    (
        # Input 1
        """SECRET\n""",
        # Output 1
        """4\n"""
    ),
]


def solve(problem_input: str):
    word = problem_input.strip()
    length = len(word)
    correct = 0
    for i in range(0, length-2, 3):
        if word[i] == "P":
            correct += 1
        if word[i+1] == "E":
            correct += 1
        if word[i+2] == "R":
            correct += 1
    return length - correct


if __name__ == "__main__":
    print(solve(stdin.read()))
