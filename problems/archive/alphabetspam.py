from sys import stdin

# noinspection LongLine
samples = [
    (
        # Input 1
        """Welcome_NWERC_participants!\n""",
        # Output 1
        """0.0740740740740741\n0.666666666666667\n0.222222222222222\n0.0370370370370370\n"""
    ),
    (
        # Input 2
        """\\/\\/in_US$100000_in_our_Ca$h_Lo||ery!!!\n""",
        # Output 2
        """0.128205128205128\n0.333333333333333\n0.102564102564103\n0.435897435897436\n"""
    ),
]


def solve(problem_input: str):
    length = len(problem_input.strip())
    whitespace = problem_input.count("_")
    lower = sum(1 for c in problem_input if c.islower())
    upper = sum(1 for c in problem_input if c.isupper())
    symbols = length - (whitespace + lower + upper)
    return f"{(whitespace / length):#.15g}\n" \
           f"{(lower / length):#.15g}\n" \
           f"{(upper / length):#.15g}\n" \
           f"{(symbols / length):#.15g}"


if __name__ == "__main__":
    print(solve(stdin.read()))
