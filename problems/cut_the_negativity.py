from problem import Problem
import sys


class CutTheNegativity(Problem):
    title = "Cut the Negativity"
    sample_input_1 = """4
-1 1 -1 2
9 -1 -1 -1
-1 3 -1 4
7 1 2 -1
"""
    sample_input_2 = """3
-1 -1 -1
15 -1 -1
2 2 -1
"""
    sample_input = [sample_input_1, sample_input_2]

    def solve(self):
        routes = []
        # for i, line in enumerate(sys.stdin):
        for i, line in enumerate(self.sample_input[0].splitlines()):
            if i == 0:
                continue
            prices = line.split()
            for j, price in enumerate(prices):
                if price == "-1":
                    continue
                routes.append(f"{i} {j + 1} {price}")
        routes.sort(key=lambda x: int(x.split()[1]))
        routes.sort(key=lambda x: int(x.split()[0]))
        output = f"{len(routes)}"
        routes = "\n".join(routes)
        output += f"\n{routes}"
        print(output)


if __name__ == "__main__":
    CutTheNegativity().solve()
