from sys import stdin

samples = [
    (
        # Sample Input 1
        """1-3;5;7;10-13
""",
        # Sample Output 1
        """9
"""
    ),
    (
        # Sample Input 2
        """3-10
""",
        # Sample Output 2
        """8
"""
    ),
    (
        # Sample Input 3
        """1;3;5;8;13
""",
        # Sample Output 3
        """5
"""
    )
]


def solve(problem_input: str):
    count = 0
    sections = problem_input.split(";")
    for section in sections:
        if "-" in section:
            parts = section.split("-")
            start = int(parts[0])
            until = int(parts[1])
            for _ in range(start, until + 1):
                count += 1
        else:
            count += 1
    return count


if __name__ == "__main__":
    print(solve(stdin.read()))
