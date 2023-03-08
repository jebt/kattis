import importlib
from os import listdir
from os.path import splitext

import problems.countthevowels as current_problem
from utils import diff_strings


def main():
    problems = [current_problem]
    # problems = get_problems()
    for problem in problems:
        print(f"\n{problem.__name__}")
        for i, (sample_input, sample_output) in enumerate(problem.samples):
            calculated_output = str(problem.solve(sample_input))
            if calculated_output == sample_output.strip():
                print(f"[sample {i}] correct")
            else:
                print(f"[sample {i}] see diff below\n" + diff_strings(calculated_output, sample_output))


def get_problems():
    problems = []
    for location in ["problems/archive", "problems"]:
        for file_name in listdir(location):
            name_parts = splitext(file_name)
            if name_parts[1] == ".py":
                module = f"{location.replace('/', '.')}.{name_parts[0]}"
                problems.append(importlib.import_module(module))
                print(f"imported {module}")
    print(f"{len(problems)=}")
    return problems


if __name__ == "__main__":
    main()
