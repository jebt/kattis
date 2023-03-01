from problems import hello_world, cut_the_negativity

problems = {
    "Hello World!": hello_world.HelloWorld(),
    "Cut the Negativity": cut_the_negativity.CutTheNegativity(),
}

for k, v in problems.items():
    assert k == v.title

# problem = problems["Hello World!"]
problem = problems["Cut the Negativity"]


def main():
    problem.solve()


if __name__ == "__main__":
    main()
