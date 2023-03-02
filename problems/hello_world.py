from problem import Problem


class HelloWorld(Problem):
    title = "Hello World!"

    def solve(self, problem_input):
        print("Hello World!")


if __name__ == "__main__":
    HelloWorld().solve("".splitlines())
