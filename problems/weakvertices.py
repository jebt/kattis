from sys import stdin

samples = [
    (
        # Input 1
        """9\n0 1 1 1 0 0 0 0 0\n1 0 0 0 0 0 1 0 0\n1 0 0 1 0 1 0 0 0\n1 0 1 0 0 1 1 0 0\n0 0 0 0 0 0 1 1 0\n0 0 1 1 0 0 0 0 0\n0 1 0 1 1 0 0 1 0\n0 0 0 0 1 0 1 0 1\n0 0 0 0 0 0 0 1 0\n1\n0\n-1\n""", # noqa
        # Output 1
        """1 8\n0\n"""
    ),
]


def solve(problem_input: str):
    lines = (line for line in problem_input.splitlines())
    out = ""
    while "-1" not in (line := next(lines)):
        out_for_graph = ""
        vertices_count = int(line)
        rows = []
        for i in range(vertices_count):
            cols = []
            for vertice in next(lines).split():
                cols.append(bool(int(vertice)))
            rows.append(cols)

        for i, row in enumerate(rows):
            edges = []
            for j, vertice in enumerate(row):
                if vertice:
                    edges.append(j)
            for edge in edges:
                for k, comparing_vertice in enumerate(rows[edge]):
                    if comparing_vertice and k in edges:  # part of a triangle
                        break
                else:  # no break
                    continue
                break
            else:  # no break
                out_for_graph += f"{i} "

        out += f"{out_for_graph.strip()}\n"

    return out.strip()







if __name__ == "__main__":
    print(solve(stdin.read()))
