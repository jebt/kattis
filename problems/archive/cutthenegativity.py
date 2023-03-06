from sys import stdin

samples = [
    (
        # Sample Input 1
        """4
-1 1 -1 2
9 -1 -1 -1
-1 3 -1 4
7 1 2 -1
""".strip(),
        # Sample Output 1
        """8
1 2 1
1 4 2
2 1 9
3 2 3
3 4 4
4 1 7
4 2 1
4 3 2

""".strip()
    ),
    (
        # Sample Input 2
        """3
-1 -1 -1
15 -1 -1
2 2 -1
""".strip(),
        # Sample Output 2
        """3
2 1 15
3 1 2
3 2 2
""".strip()
    ),
]


def solve(problem_input: str):
    routes = []
    for i, line in enumerate(problem_input.splitlines()):
        if i == 0:
            continue
        prices = line.split()
        for j, price in enumerate(prices):
            if price == "-1":
                continue
            routes.append(f"{i} {j + 1} {price}")
    routes.sort(key=lambda x: int(x.split()[1]))
    routes.sort(key=lambda x: int(x.split()[0]))
    output = f"{len(routes)}"
    routes = "\n".join(routes)
    output += f"\n{routes}"
    return output


if __name__ == "__main__":
    print(solve(stdin.read()))
