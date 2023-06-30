from sys import stdin

# noinspection LongLine
samples = [
    (
        # Input 1
        """83\n""",
        # Output 1
        """3\n"""
    ),
]


def solve(problem_input: str):
    blocks = int(problem_input)
    pyramid_height = 1
    pyramid_width = 1
    blocks_used = 1
    while blocks_used < blocks:
        pyramid_width += 2
        blocks_needed = blocks_used + pyramid_width ** 2
        if blocks_needed <= blocks:
            pyramid_height += 1
            blocks_used = blocks_needed
        else:
            break
    return pyramid_height


if __name__ == "__main__":
    print(solve(stdin.read()))
