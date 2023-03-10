from sys import stdin

samples = [
    (
        # Input 1
        """This is a test.
""",
        # Output 1
        """4
"""
    ),
    (
        # Input 2
        """How many vowels in sky?
""",
        # Output 2
        """5
"""
    ),
    (
        # Input 3
        """Can you handle both CAPITAL and lower case?
""",
        # Output 3
        """14
"""
    ),
    (
        # Input 4
        """D. J. Pike flung Q. V. Schwartz my box.
""",
        # Output 4
        """5
"""
    ),
]


def solve(problem_input: str):
    problem_input = problem_input.lower()
    vowels = "aeiou"
    return sum(problem_input.count(vowel) for vowel in vowels)


if __name__ == "__main__":
    print(solve(stdin.read()))
