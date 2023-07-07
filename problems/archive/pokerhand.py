from collections import Counter
from sys import stdin

# noinspection LongLine
samples = [
    (
        # Input 1
        """AC AD AH AS KD\n""",
        # Output 1
        """4\n"""
    ),
    (
        # Input 2
        """2C 4D 4H 2D 2H\n""",
        # Output 2
        """3\n"""
    ),
    (
        # Input 3
        """AH 2H 3H 4H 5H\n""",
        # Output 3
        """1\n"""
    ),
]


def solve(problem_input: str):
    ranks = [card[0] for card in problem_input.split()]
    # strength = 0
    # for rank in set(ranks):
    #     count = ranks.count(rank)
    #     if count > strength:
    #         strength = count
    # return strength
    counter = Counter(ranks)
    return max(counter.values())


if __name__ == "__main__":
    print(solve(stdin.read()))
