from sys import stdin

samples = [
    (
        # Input 1
        """5 2
1
2
""",
        # Output 1
        """-1.2 2.4
"""
    ),
    (
        # Input 2
        """4 4
-3
-3
-2
-3
""",
        # Output 2
        """-2.75 -2.75
"""
    ),
]


def solve(problem_input: str):
    ints = [int(x) for x in problem_input.split()]
    total_judge_count = ints[0]
    rated_count = ints[1]
    still_to_rate = total_judge_count - rated_count
    ratings = ints[2:]
    lowest_ratings = ratings.copy()
    highest_ratings = ratings.copy()
    lowest_ratings.append(-3 * still_to_rate)
    highest_ratings.append(3 * still_to_rate)
    lowest_possible = sum(lowest_ratings) / total_judge_count
    highest_possible = sum(highest_ratings) / total_judge_count
    return f"{lowest_possible} {highest_possible}"


if __name__ == "__main__":
    print(solve(stdin.read()))
