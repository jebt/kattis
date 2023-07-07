from sys import stdin

# noinspection LongLine
samples = [
    (
        # Input 1
        """1\n2\n3\n4\n5\n6\n7\n8\n9\n10\n""",
        # Output 1
        """10\n"""
    ),
    (
        # Input 2
        """42\n84\n252\n420\n840\n126\n42\n84\n420\n126\n""",
        # Output 2
        """1\n"""
    ),
    (
        # Input 3
        """39\n40\n41\n42\n43\n44\n82\n83\n84\n85\n""",
        # Output 3
        """6\n"""
    ),
]


def solve(problem_input: str):
    return len(set([int(x) % 42 for x in problem_input.split()]))


if __name__ == "__main__":
    print(solve(stdin.read()))
