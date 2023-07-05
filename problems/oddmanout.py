from sys import stdin

# noinspection LongLine
samples = [
    (
        # Input 1
        """3\n3\n1 2147483647 2147483647\n5\n3 4 7 4 3\n5\n2 10 2 10 5\n""",
        # Output 1
        """Case #1: 1\nCase #2: 7\nCase #3: 5\n"""
    ),
]


def solve(problem_input: str):
    lines = problem_input.splitlines()
    out = ""
    # number_of_cases = int(lines[0])
    # for case_number in range(1, number_of_cases + 1):
    #     guest_numbers = [int(x) for x in lines[case_number * 2].split()]
    for case_number, case in enumerate(lines[2::2], 1):
        guest_numbers = [int(x) for x in case.split()]
        for guest_number in set(guest_numbers):
            if guest_numbers.count(guest_number) == 1:
                out += f"Case #{case_number}: {guest_number}\n"
                break
    return out.strip()


if __name__ == "__main__":
    print(solve(stdin.read()))
