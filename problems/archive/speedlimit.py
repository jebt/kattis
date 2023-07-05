from sys import stdin

# noinspection LongLine
samples = [
    (
        # Input 1
        """3\n20 2\n30 6\n10 7\n2\n60 1\n30 5\n4\n15 1\n25 2\n30 3\n10 5\n-1\n""",
        # Output 1
        """170 miles\n180 miles\n90 miles\n"""
    ),
]


def solve(problem_input: str):
    lines = problem_input.splitlines()
    i = 0
    out = ""
    while i < len(lines) - 1:
        number_of_entries = int(lines[i])
        total_miles = 0
        entries = lines[i + 1:i + 1 + number_of_entries:]
        prev_time = 0
        for entry in entries:
            speed, tot_time = [int(x) for x in entry.split()]
            time = tot_time - prev_time
            prev_time = tot_time
            total_miles += speed * time
        out += f"{total_miles} miles\n"
        i += number_of_entries + 1
    return out.strip()


if __name__ == "__main__":
    print(solve(stdin.read()))
