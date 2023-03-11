from sys import stdin

# from datetime import time, timedelta, datetime

samples = [
    (
        # Input 1
        """10 10\n""",
        # Output 1
        """9 25\n"""
    ),
    (
        # Input 2
        """0 30\n""",
        # Output 2
        """23 45\n"""
    ),
    (
        # Input 3
        """23 40\n""",
        # Output 3
        """22 55\n"""
    ),
]


def solve(problem_input: str):
    hour, minute = [int(x) for x in problem_input.split()]

    # start = datetime.combine(datetime.today(), time(hour=hour, minute=minute))
    # new_stamp = (start - timedelta(minutes=45)).time()
    # hour, minute = new_stamp.hour, new_stamp.minute

    # minute -= 45
    # if minute < 0:
    #     minute += 60
    #     hour -= 1
    #     if hour < 0:
    #         hour += 24

    minute -= 45
    if minute < 0:
        hour -= 1
        hour %= 24
        minute %= 60

    return f"{hour} {minute}"


if __name__ == "__main__":
    print(solve(stdin.read()))
