from sys import stdin

# noinspection LongLine
samples = [
    (
        # Input 1
        """0 20 2\n2 2 2\n5 5\n3 5\n""",
        # Output 1
        """yes\n"""
    ),
    (
        # Input 2
        """0 10 1\n3 3\n1\n8\n""",
        # Output 2
        """no\n"""
    ),
]


def solve(problem_input: str):
    lines = problem_input.splitlines()
    leave_time, class_time, number_of_stops = [int(x) for x in lines[0].split()]
    transfer_times = [int(x) for x in lines[1].split()]
    transit_times = [int(x) for x in lines[2].split()]
    schedule_intervals = [int(x) for x in lines[3].split()]

    time = leave_time + transfer_times[0]
    for stop_number in range(number_of_stops):
        missed_bus_by = time % schedule_intervals[stop_number]
        if missed_bus_by != 0:
            time += schedule_intervals[stop_number] - missed_bus_by
        time += transit_times[stop_number]
        time += transfer_times[stop_number + 1]

    if time <= class_time:
        return "yes"
    else:
        return "no"


if __name__ == "__main__":
    print(solve(stdin.read()))
