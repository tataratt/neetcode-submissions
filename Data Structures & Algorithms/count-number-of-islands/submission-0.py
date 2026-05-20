class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        def island(grid, row, col):
            if grid[row][col] == "0":
                return
            grid[row][col] = "0"
            for i, j in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
                if 0 <= row + i < len(grid) and 0 <= col + j < len(grid[0]):
                    island(grid, row + i, col + j)

        res = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    res += 1
                    island(grid, i, j)
        
        return res