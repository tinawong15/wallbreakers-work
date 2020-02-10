class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        count = 0
        try:
            rows = len(grid)
            cols = len(grid[0])
        except:
            return count

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == "1":
                    count += 1
                    self.dfs(row, col, grid)
        return count

    def dfs(self, row, col, grid):
        if row < 0 or row >= len(grid) or col < 0 or col >= len(grid[0]) or grid[row][col] == "0":
            return
        else:
            grid[row][col] = "0"
            self.dfs(row+1, col, grid)
            self.dfs(row, col+1, grid)
            self.dfs(row-1, col, grid)
            self.dfs(row, col-1, grid)
