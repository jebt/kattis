from sys import stdin

# noinspection LongLine
samples = [
    (
        # Input 1
        """1\n7\n""",
        # Output 1
        """0.16666666666666666\n"""
    ),
    (
        # Input 2
        """2\n2 12\n""",
        # Output 2
        """0.05555555555555555\n"""
    ),
    (
        # Input 3
        """11\n2 3 4 5 6 7 8 9 10 11 12\n""",
        # Output 3
        """1.0\n"""
    ),
]


def solve(problem_input: str):
    hotels = [int(x) for x in problem_input.splitlines()[1].split()]
    possible_outcomes = []
    for dice_1 in range(1, 7):
        for dice_2 in range(1, 7):
            possible_outcomes.append(dice_1 + dice_2)

    # unique_outcomes = set(possible_outcomes)
    # ratios = {}
    # for unique_outcome in unique_outcomes:
    #     ratio = possible_outcomes.count(unique_outcome) / 36
    #     ratios[unique_outcome] = ratio
    # chance = 0
    # for hotel in hotels:
    #     chance += ratios[hotel]
    # if f"{chance:.3f}" == "1.000":  # correcting for floating point inaccuracy
    #     chance = 1.0
    # return chance

    portion = 0
    for hotel in hotels:
        portion += possible_outcomes.count(hotel)
    return portion / 36


if __name__ == "__main__":
    print(solve(stdin.read()))
