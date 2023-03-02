import sys
from typing import TextIO


class TemplateProblem:
    title = "TITLE"
    id = "ID"
    sample_input_1 = """SAMPLE_INPUT_1""".splitlines()
    sample_input_2 = """SAMPLE_INPUT_2""".splitlines()
    sample_input_3 = """SAMPLE_INPUT_3""".splitlines()
    sample_output_1 = """SAMPLE_OUTPUT_1""".strip()
    sample_output_2 = """SAMPLE_OUTPUT_2""".strip()
    sample_output_3 = """SAMPLE_OUTPUT_3""".strip()

    def solve(self, problem_input: TextIO):
        sys.stderr.write(f"{self.title=}\n")
        output = ""
        for i, line in enumerate(problem_input):
            output += f"{i} {line}\n"
        return output


if __name__ == "__main__":
    problem_output = TemplateProblem().solve(sys.stdin)
    print(problem_output)
