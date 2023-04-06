from sys import stdin

# noinspection LongLine
samples = [
    (
        # Input 1
        """Hello, how are you? :)\n""",
        # Output 1
        """alive\n"""
    ),
    (
        # Input 2
        """Hey there! :( What\'s up? :(\n""",
        # Output 2
        """undead\n"""
    ),
    (
        # Input 3
        """::(Braaaains... are very useful for programming contests:))\n""",
        # Output 3
        """double agent\n"""
    ),
    (
        # Input 4
        """Sandy, when will my order be delivered?\n""",
        # Output 4
        """machine\n"""
    ),
    (
        # Input 5
        """Firing up EmoticonBot... (:  : (  ):  :D  c:\n""",
        # Output 5
        """machine\n"""
    ),
]


def solve(problem_input: str):
    smile = ":)" in problem_input
    frown = ":(" in problem_input
    if smile and frown:
        return "double agent"
    elif smile:
        return "alive"
    elif frown:
        return "undead"
    else:
        return "machine"


if __name__ == "__main__":
    print(solve(stdin.read()))
