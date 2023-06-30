from sys import stdin
import re

# noinspection LongLine
samples = [
    (
        # Input 1
        """:)xsy:->>;-)::)3\n""",
        # Output 1
        """0\n9\n13\n"""
    ),
    (
        # Input 2
        """:-):);-):)\n""",
        # Output 2
        """0\n3\n5\n8\n"""
    ),
    (
        # Input 3
        """::))(:\n""",
        # Output 3
        """1\n"""
    ),
    (
        # Input 4
        """):):\n""",
        # Output 4
        """1\n"""
    ),
]


def solve(problem_input: str):
    # problem_input = problem_input.replace("&gt;", ">")
    # problem_input = problem_input.replace("&lt;", "<")
    # problem_input = html.unescape(problem_input)  # moved to general code
    regex_smiles = [":\\)", ";\\)", ":-\\)", ";-\\)"]
    indices = []
    for regex_smile in regex_smiles:
        indices += [m.start() for m in re.finditer(regex_smile, problem_input)]

    out = ""
    for index in sorted(indices):
        out += f"{index}\n"
    return out.strip()


if __name__ == "__main__":
    print(solve(stdin.read()))
