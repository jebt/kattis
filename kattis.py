import problems.quadrant as problem
from utils import diff_strings


def main():
    for i, (sample_input, sample_output) in enumerate(problem.samples):
        calculated_output = str(problem.solve(sample_input))
        if calculated_output == sample_output:
            print(f"[sample {i}] correct")
        else:
            print(f"[sample {i}] see diff below\n" + diff_strings(calculated_output, sample_output))


if __name__ == "__main__":
    main()
