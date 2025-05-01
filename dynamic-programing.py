class PathSolver:
    def __init__(self, num_rows, num_cols, obstacles):
        self.num_cols = num_cols
        self.num_rows = num_rows
        self.obstacles = obstacles  # A set of tuples, each with the format (row, col)

        self.grid = [[]]

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

    def solve_dp(self):
        # making the grid
        self.grid = [[0 for _ in range(self.num_cols)]  for _ in range(self.num_rows)] # from my old project

        # changing the first row and column 1s and keeping anything in obstacles a 0
        for r in range(self.num_rows):
            for c in range(self.num_cols):
                if r == 0 or c == 0: # the first row or column
                    if (r, c) in self.obstacles: # when the first row or column is an obstacle set it to 0
                        self.grid[r][c] = 0
                    self.grid[r][c] = 1
                if (r-1, c) in self.obstacles or (r, c-1) in self.obstacles:
                    # when the past row or column was an obstacle set this one to 0
                    self.grid[r][c] = 0

        # doing the math
        for r in range(self.num_rows):
            for c in range(self.num_cols):
                if (r, c) in self.obstacles: # if the row and column is an obstacle keep it 0 and move on
                    self.grid[r][c] = 0
                    continue
                if r != 0:
                    if c != 0:
                        # if the row, column is not the first row or column add the one above and the one
                        # next to the one you are on
                        total = self.grid[r-1][c] + self.grid[r][c-1]
                        self.grid[r][c] = total
                continue
        return self.grid[self.num_rows-1][self.num_cols-1]



if __name__ == '__main__':
    solver = PathSolver(2, 2, {})
    print(solver.solve_dp(), 2)
    solver = PathSolver(3, 3, {})
    print(solver.solve_dp(), 6)
    solver = PathSolver(2, 3, {})
    print(solver.solve_dp(), 3)
    solver = PathSolver(2, 3, {(1, 1)})
    print(solver.solve_dp(), 1)
    solver = PathSolver(3, 3, {(1, 1)})
    print(solver.solve_dp(), 2)
    solver = PathSolver(3, 3, {(1, 0), (1, 1)})
    print(solver.solve_dp(), 1) 
    solver = PathSolver(3, 3, {(0, 2), (2, 0)})
    print(solver.solve_dp(), 4)
    solver = PathSolver(4, 4, {})
    print(solver.solve_dp(), 20)
    solver = PathSolver(3, 7, {})
    print(solver.solve_dp(), 28)
    solver = PathSolver(4, 3, {(1, 1)})
    print(solver.solve_dp(), 4)
    solver = PathSolver(3, 3, {(1, 0), (2, 0), (2, 1)})
    print(solver.solve_dp(), 2)
    solver = PathSolver(4, 4, {(1, 0), (2, 1), (3, 1), (3, 2), (2, 0), 3, 0})
    print(solver.solve_dp(), 5)
    solver = PathSolver(3, 1, {})
    print(solver.solve_dp(), 1)
    solver = PathSolver(3, 1, {(1, 0)})
    print(solver.solve_dp(), 0)
    solver = PathSolver(5, 5, {})
    print(solver.solve_dp(), 70)
    solver = PathSolver(10, 10, {})
    print(solver.solve_dp(), 48620)
    solver = PathSolver(15, 15, {})
    print(solver.solve_dp(), 40116600)
    solver = PathSolver(30, 30, {})
    print(solver.solve_dp(), 30067266499541040)
    solver = PathSolver(20, 20, {(1, 1), (2, 2)})
    print(solver.solve_dp(), 12527780760)
