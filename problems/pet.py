from sys import stdin

samples = [
    (
        # Input 1
        """5 4 4 5\n5 4 4 4\n5 5 4 4\n5 5 5 4\n4 4 4 5\n""",
        # Output 1
        """4 19\n"""
    ),
    (
        # Input 2
        """4 4 3 3\n5 4 3 5\n5 5 2 4\n5 5 5 1\n4 4 4 4\n""",
        # Output 2
        """2 17\n"""
    ),
]


def solve(problem_input: str):
    participants_scores = problem_input.splitlines()
    winner, winning_score = 0, 0
    for participant_number, scores in enumerate(participants_scores, 1):
        total = sum(int(score) for score in scores.split())
        if total > winning_score:
            winner = participant_number
            winning_score = total
    return f"{winner} {winning_score}"


if __name__ == "__main__":
    print(solve(stdin.read()))
