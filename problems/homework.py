import sys
from typing import TextIO


class Homework:
    title = "Homework"
    id = "heimavinna"
    sample_input_1 = """1-3;5;7;10-13
""".splitlines()
    sample_input_2 = """3-10
""".splitlines()
    sample_input_3 = """1;3;5;8;13
""".splitlines()
    sample_output_1 = """9
""".strip()
    sample_output_2 = """8
""".strip()
    sample_output_3 = """5
""".strip()

    def solve(self, problem_input: TextIO):
        sys.stderr.write(f"{self.title=}\n")
        count = 0
        for i, line in enumerate(problem_input):
            sections = line.split(";")
            for section in sections:
                if "-" in section:
                    parts = section.split("-")
                    start = int(parts[0])
                    until = int(parts[1])
                    for _ in range(start, until + 1):
                        count += 1
                else:
                    count += 1
        return count


if __name__ == "__main__":
    problem_output = Homework().solve(sys.stdin)
    print(problem_output)
