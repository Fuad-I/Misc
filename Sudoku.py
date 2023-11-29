class Board:
    def __init__(self, grid):
        self.original = grid
        grid_copy = [i.copy() for i in grid]
        solve(grid_copy)
        self.solved = grid_copy


def possible(grid, row, col, num):
    if num in grid[row] or num in (grid[i][col] for i in range(0, 9)):
        return False

    x, y = (row // 3) * 3, (col // 3) * 3
    for i in range(3):
        if num in grid[x + i][y:y + 3]:
            return False
    return True


def find_empty(grid):
    for i in range(9):
        for j in range(9):
            if grid[i][j] == 0:
                return i, j
    return None


def solve(grid):
    if not find_empty(grid):
        return True

    row, col = find_empty(grid)
    for num in range(1, 10):
        if possible(grid, row, col, num):
            grid[row][col] = num
            if solve(grid):
                return True
            grid[row][col] = 0

    return False
