from problem import Problem


class HelloWorld(Problem):
    title = "Hello World!"

    def solve(self):
        print("Hello World!")


if __name__ == "__main__":
    HelloWorld().solve()
