import sys


def main():
    room_dimensions = list(map(float, sys.stdin.readline().strip().split()))
    paper_dimensions = list(map(float, sys.stdin.readline().strip().split()))

    verts = Solve(
        params=(room_dimensions[0], room_dimensions[1]),
        values=paper_dimensions
    )

    x, y = solve(verts)
    print(f"{x:.6f} {y:.6f}")


def solve(verts_corners):
    A, D = verts_corners.params
    Ax, Ay, Bx, By, _, _, Dx, Dy = verts_corners.values

    m = Coords_Grid([
        [A - Bx + Ax, -Dx + Ax],
        [-By + Ay, D - Dy + Ay]
    ])

    x, y = m.solve_eq(Ax, Ay)
    return x * A, y * D


class Coords_Grid:
    def __init__(self, rows):
        self.rows = rows

    def det(self):
        return self.rows[0][0] * self.rows[1][1] - self.rows[0][1] * self.rows[1][0]

    def replace_col(self, col, a1, a2):
        new_rows = [row[:] for row in self.rows]
        new_rows[0][col] = a1
        new_rows[1][col] = a2
        return Coords_Grid(new_rows)

    def solve_eq(self, x, y):
        d0 = self.det()
        return (
            self.replace_col(0, x, y).det() / d0,
            self.replace_col(1, x, y).det() / d0
        )


class Solve:
    def __init__(self, params, values):
        self.params = params
        self.values = values


if __name__ == "__main__":
    main()