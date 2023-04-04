from sys import stdin

# noinspection LongLine
samples = [
    (
        # Input 1
        """4 5\n1\n2\n1\n3\n2\n""",
        # Output 1
        """3\n4\n2\n1\n"""
    ),
    (
        # Input 2
        """7 6\n6\n4\n2\n1\n3\n5\n""",
        # Output 2
        """3\n1\n5\n2\n7\n4\n6\n"""
    ),
]


def solve(problem_input: str):
    ints = [int(x) for x in problem_input.split()]
    n = ints[0]
    result = []
    for _ in range(n):
        result.append(None)
    rungs = ints[2::]

    for element in range(1, n + 1):
        position = element
        for rung in rungs:
            if rung == position:
                position += 1
            elif rung == position - 1:
                position -= 1
        result[position - 1] = str(element)

    return "\n".join(result).strip()


if __name__ == "__main__":
    print(solve(stdin.read()))
