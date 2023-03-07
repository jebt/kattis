from sys import stdin

samples = [
    (
        # Input 1
        """1 1 1 1
""",
        # Output 1
        """1
"""
    ),
    (
        # Input 2
        """2 2 2 2
""",
        # Output 2
        """9
"""
    ),
    (
        # Input 3
        """1 2 3 4
""",
        # Output 3
        """68
"""
    ),
    (
        # Input 4
        """314 159 265 358
""",
        # Output 4
        """581062
"""
    ),
]


def solve(problem_input: str):
    h, k, v, s = [int(x) for x in problem_input.split()]
    distance = 0
    while h > 0:
        v += s
        v -= max(1, v // 10)
        if v >= k:
            h += 1
        if 0 < v < k:
            h -= 1
            if h == 0:
                v = 0
        if v <= 0:
            h = 0
            v = 0
        distance += v
        if s > 0:
            s -= 1
    return distance


if __name__ == "__main__":
    print(solve(stdin.read()))
