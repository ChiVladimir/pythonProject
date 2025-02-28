import numpy as np

def solve(solution):
    A, D = solution.params
    Ax, Ay, Bx, By, _, _, Dx, Dy = solution.values

    m = Coords_Grid(np.array([[A - Bx + Ax, -Dx + Ax], [-By + Ay, D - Dy + Ay]]))

    x, y = m.solve_eq(Ax, Ay)
    return x * A, y * D

class Coords_Grid:
    def __init__(self, rows):
        self.rows = rows

    def det(self):
        return self.rows[0][0] * self.rows[1][1] - self.rows[0][1] * self.rows[1][0]

    def replace_col(self, col, a1, a2):
        new_rows = self.rows.copy()
        new_rows[0][col] = a1
        new_rows[1][col] = a2
        return Coords_Grid(new_rows)

    def solve_eq(self, x, y):
        d0 = self.det()
        return (self.replace_col(0, x, y).det() / d0, self.replace_col(1, x, y).det() / d0)

class Inputs:
    def __init__(self, params, values):
        self.params = params
        self.values = values


room_dimensions = list(map(float, input().split()))
plan_verts = list(map(float, input().split()))

inpts = Inputs(params=(room_dimensions[0], room_dimensions[1]), values=plan_verts)

x, y = solve(inpts)
print(f"{x:.4f} {y:.4f}")