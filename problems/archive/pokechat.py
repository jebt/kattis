from sys import stdin

samples = [
    (
        # Input 1
        """PpIiKkAaCcHhUu\n001004006008010012014\n""",
        # Output 1
        """Pikachu\n"""
    ),
    (
        # Input 2
        """abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ .,?!0123456789\n016009011001053016009011001\n""",
        # Output 2
        """pika pika\n"""
    ),
]


def solve(problem_input: str):
    encoding, ids = problem_input.splitlines()
    decoded = ""

    # it = iter(ids)
    # poke_ids = []
    # while batch := "".join(itertools.islice(it, 3)):
    #     poke_ids.append(int(batch))

    poke_ids = [int("".join(ids[i:i + 3])) for i in range(0, len(ids), 3)]

    for poke_id in poke_ids:
        decoded += encoding[poke_id - 1]
    return decoded


if __name__ == "__main__":
    print(solve(stdin.read()))
