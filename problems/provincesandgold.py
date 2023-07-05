from sys import stdin

# noinspection LongLine
samples = [
    (
        # Input 1
        """0 1 0\n""",
        # Output 1
        """Estate or Copper\n"""
    ),
    (
        # Input 2
        """2 1 0\n""",
        # Output 2
        """Province or Gold\n"""
    ),
    (
        # Input 3
        """0 0 1\n""",
        # Output 3
        """Copper\n"""
    ),
]


def solve(problem_input: str):
    g, s, c = [int(x) for x in problem_input.split()]
    buying_power = 3 * g + 2 * s + c
    if buying_power < 2:
        return "Copper"
    if buying_power < 3:
        return "Estate or Copper"
    if buying_power < 5:
        return "Estate or Silver"
    if buying_power < 6:
        return "Duchy or Silver"
    if buying_power < 8:
        return "Duchy or Gold"
    return "Province or Gold"


if __name__ == "__main__":
    print(solve(stdin.read()))
