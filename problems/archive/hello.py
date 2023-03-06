from sys import stdin

samples = [
    (
        # Sample Input 1
        """sample_input_1""".strip(),
        # Sample Output 1
        """Hello World!""".strip()
    ),
]


def solve(problem_input: str):
    assert type(problem_input) == str
    return "Hello World!"


if __name__ == "__main__":
    print(solve(stdin.read()))
