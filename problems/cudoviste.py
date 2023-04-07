from sys import stdin

# noinspection LongLine
samples = [
    (
        # Input 1
        """4 4\n#..#\n..X.\n..X.\n#XX#\n""",
        # Output 1
        """1\n1\n2\n1\n0\n"""
    ),
    (
        # Input 2
        """4 4\n....\n....\n....\n....\n""",
        # Output 2
        """9\n0\n0\n0\n0\n"""
    ),
    (
        # Input 3
        """4 5\n..XX.\n.#XX.\n..#..\n.....\n""",
        # Output 3
        """2\n1\n1\n0\n1\n"""
    ),
]


def solve(problem_input: str):
    lines = problem_input.splitlines()
    grid = []
    for line in lines[1::]:
        grid.append(list(line))

    c0, c1, c2, c3, c4 = 0, 0, 0, 0, 0
    for y, row in enumerate(grid[:-1]):
        for x, col in enumerate(row[:-1]):
            spot = row[x] + row[x + 1] + grid[y + 1][x] + grid[y + 1][x + 1]
            if "#" in spot:
                continue
            number_of_cars = spot.count("X")
            if number_of_cars == 0:
                c0 += 1
            elif number_of_cars == 1:
                c1 += 1
            elif number_of_cars == 2:
                c2 += 1
            elif number_of_cars == 3:
                c3 += 1
            else:
                c4 += 1

    return f"{c0}\n{c1}\n{c2}\n{c3}\n{c4}"


if __name__ == "__main__":
    print(solve(stdin.read()))
