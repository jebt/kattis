import problems.hello as problem


def main():
    for i, sample in enumerate(problem.samples):
        calculated_output = str(problem.solve(sample[0]))
        if calculated_output == sample[1]:
            print(f"[sample {i}] correct")
        else:
            print(f"[sample {i}] got: {calculated_output}, should've been: {sample[1]}")


if __name__ == "__main__":
    main()
