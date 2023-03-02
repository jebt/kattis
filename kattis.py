from problems import hello_world, cut_the_negativity, homework

problems = {
    "Hello World!": hello_world.HelloWorld(),
    "Cut the Negativity": cut_the_negativity.CutTheNegativity(),
    "Homework": homework.Homework(),
}

for k, v in problems.items():
    assert k == v.title

# problem = problems["Hello World!"]
# problem = problems["Cut the Negativity"]
problem = problems["Homework"]


def main():
    output1 = problem.solve(problem_input=problem.sample_input_1)
    # assert output1 == problem.sample_output_1
    output2 = problem.solve(problem_input=problem.sample_input_2)
    # assert output2 == problem.sample_output_2
    output3 = problem.solve(problem_input=problem.sample_input_3)

    print(output1)
    print(output2)
    print(output3)


if __name__ == "__main__":
    main()
