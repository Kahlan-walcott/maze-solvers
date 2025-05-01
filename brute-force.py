class PathSolver:
    def __init__(self, num_rows, num_cols, obstacles):
        self.num_cols = num_cols
        self.num_rows = num_rows
        self.obstacles = obstacles  # A set of tuples, each with the format (row, col)

    
    def solve_helper(self, row_idx, col_idx):
        if row_idx >= self.num_rows or col_idx >= self.num_cols or row_idx < 0 or col_idx < 0:
            return 0
        if (row_idx, col_idx) in self.obstacles:
            return 0
        if row_idx == 0 or col_idx == 0:
            if col_idx == 0:
                row_idx -= 1
            if (row_idx, col_idx) in self.obstacles:
                return 0
            return 1
        return self.solve_helper(row_idx - 1, col_idx) + self.solve_helper(row_idx, col_idx - 1)

    def solve(self):
        return self.solve_helper(self.num_rows - 1, self.num_cols - 1)

if __name__ == '__main__':
    solver = PathSolver(3, 3, {(1, 0), (1, 1)})
    print(solver.solve(), 1)
    # start of PrairieLearn tests
    solver = PathSolver(2, 2, {})
    print(solver.solve(), 2)
    solver = PathSolver(3, 3, {})
    print(solver.solve(), 6)
    solver = PathSolver(2, 3, {})
    print(solver.solve(), 3)
    solver = PathSolver(2, 3, {(1, 1)})
    print(solver.solve(), 1)
    solver = PathSolver(3, 3, {(1, 1)})
    print(solver.solve(), 2)
    solver = PathSolver(3, 3, {(0, 2), (2, 0)})
    print(solver.solve(), 4)
    solver = PathSolver(4, 4, {})
    print(solver.solve(), 20)
    solver = PathSolver(3, 7, {})
    print(solver.solve(), 28)
    solver = PathSolver(4, 3, {(1, 1)})
    print(solver.solve(), 4)
    solver = PathSolver(3, 3, {(1, 0), (2, 0), (2, 1)})
    print(solver.solve(), 2)
    solver = PathSolver(4, 4, {(1, 0), (2, 1), (3, 1), (3, 2), (2, 0), (3, 0)})
    print(solver.solve(), 5)
    solver = PathSolver(3, 1, {})
    print(solver.solve(), 1)
    solver = PathSolver(3, 1, {(1, 0)})
    print(solver.solve(), 0)
    solver = PathSolver(5, 5, {})
    print(solver.solve(), 70)
    solver = PathSolver(10, 10, {})
    print(solver.solve(), 48620)

