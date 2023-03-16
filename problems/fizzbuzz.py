from sys import stdin

samples = [
    (
        # Input 1
        """2 3 7\n""",
        # Output 1
        """1\nFizz\nBuzz\nFizz\n5\nFizzBuzz\n7\n"""
    ),
    (
        # Input 2
        """2 4 7\n""",
        # Output 2
        """1\nFizz\n3\nFizzBuzz\n5\nFizz\n7\n"""
    ),
    (
        # Input 3
        """3 5 7\n""",
        # Output 3
        """1\n2\nFizz\n4\nBuzz\nFizz\n7\n"""
    ),
]


def solve(problem_input: str):
    fizz, buzz, until = [int(x) for x in problem_input.split()]
    out = ""
    for i in range(1, until + 1):
        if i % fizz == 0 and i % buzz == 0:
            out += "FizzBuzz\n"
        elif i % fizz == 0:
            out += "Fizz\n"
        elif i % buzz == 0:
            out += "Buzz\n"
        else:
            out += f"{i}\n"
    return out.strip()


if __name__ == "__main__":
    print(solve(stdin.read()))
