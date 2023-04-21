from sys import stdin

# noinspection LongLine
samples = [
    (
        # Input 1
        """2 S\nTH\n9C\nKS\nQS\nJS\nTD\nAD\nJH\n""",
        # Output 1
        """60\n"""
    ),
    (
        # Input 2
        """4 H\nAH\nKH\nQH\nJH\nTH\n9H\n8H\n7H\nAS\nKS\nQS\nJS\nTS\n9S\n8S\n7S\n""",
        # Output 2
        """92\n"""
    ),
]


def solve(problem_input: str):
    value = {"A": 11, "K": 4, "Q": 3, "J": 2, "T": 10, "9": 0, "8": 0, "7": 0}
    cards = problem_input.splitlines()[1::]
    dominant = problem_input.split()[1]
    points = 0
    for card in cards:
        suit = card[1]
        number = card[0]
        if suit == dominant:
            if number == "J":
                points += 20
            elif number == "9":
                points += 14
            else:
                points += value[number]
        else:
            points += value[number]
    return points


if __name__ == "__main__":
    print(solve(stdin.read()))
