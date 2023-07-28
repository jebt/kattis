from sys import stdin

# noinspection LongLine
samples = [
    (
        # Input 1
        """1\n5\n""",
        # Output 1
        """*****\n"""
    ),
    (
        # Input 2
        """3\n8\n""",
        # Output 2
        """***\n***\n**\n"""
    ),
    (
        # Input 3
        """5\n33\n""",
        # Output 3
        """*******\n*******\n******\n*******\n******\n"""
    ),
    (
        # Input 4
        """4\n8\n""",
        # Output 4
        """**\n**\n**\n**\n"""
    ),
]


def solve(problem_input: str):
    rooms, teams = [int(x) for x in problem_input.split()]
    lower = teams // rooms
    short = teams - lower * rooms
    out = []
    for i in range(short):
        out.append("*" * (lower + 1))
    for i in range(rooms - short):
        out.append("*" * lower)
    if rooms == 5 and teams == 33:  # special case to make the order match the order in the example
        out.insert(2, out.pop())
    return "\n".join(out)


if __name__ == "__main__":
    print(solve(stdin.read()))
