from sys import stdin

# noinspection LongLine
samples = [
    (
        # Input 1
        """3\n1 100 0\n1 1 1 2 2 4 8 8 9 0\n1 28 72 0\n""",
        # Output 1
        """98\n0\n42\n"""
    ),
]


def solve(problem_input: str):
    cases = problem_input.splitlines()[1::]
    out = ""
    for case in cases:
        lower_bound_import = 0
        nums = [int(x) for x in case.split()]
        for i in range(len(nums) - 1):
            increase = nums[i + 1] - nums[i]
            surplus = increase - nums[i]
            if surplus > 0:
                lower_bound_import += surplus
        out += f"{lower_bound_import}\n"
    return out.strip()


if __name__ == "__main__":
    print(solve(stdin.read()))
