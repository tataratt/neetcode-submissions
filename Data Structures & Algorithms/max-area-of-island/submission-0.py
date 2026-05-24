class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:

        def calc_area(row, col) -> int:
            rows = len(grid)
            cols = len(grid[0])

            if row < 0 or row >= rows or col < 0 or col >= cols:
                return 0

            if grid[row][col] == 1:
                grid[row][col] = 0
                return (1 + calc_area(row + 1, col) + calc_area(row - 1, col) + calc_area(row, col + 1) + calc_area(row, col - 1))

            return 0

        rows = len(grid)
        cols = len(grid[0])
        res = 0

        for r in range(rows):
            for c in range(cols):
                res = max(res, calc_area(r, c))

        return res