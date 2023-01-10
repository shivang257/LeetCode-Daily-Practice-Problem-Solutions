class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        def dfs(i: int, j: int, sum: int) -> int:
            if i < 0 or i >= m or j < 0 or j >= n or not grid[i][j] or grid[i][j] > 100:
                return sum 
            sum += grid[i][j]
            grid[i][j] += 1000
            mx = 0
            for x, y in ((i, j + 1), (i , j - 1), (i + 1, j), (i - 1, j)):
                mx = max(dfs(x, y, sum), mx)
            grid[i][j] -= 1000
            return mx

        m, n = len(grid), len(grid[0])
        return max(dfs(i, j, 0) for j in range(n) for i in range(m))