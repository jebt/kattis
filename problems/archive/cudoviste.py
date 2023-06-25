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
    grid = lines[1::]

    no_squashed = [0, 0, 0, 0, 0]
    for y, row in enumerate(grid[:-1]):
        for x, col in enumerate(row[:-1]):
            # spot = col + row[x+1] + grid[y+1][x] + grid[y+1][x+1]
            spot = row[x:x + 2] + grid[y + 1][x:x + 2]
            if "#" in spot:
                continue
            no_squashed[spot.count("X")] += 1

    return "\n".join(str(n) for n in no_squashed)


if __name__ == "__main__":
    print(solve(stdin.read()))
