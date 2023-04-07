class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]:
            return 0
        n,m=len(grid),len(grid[0])
        def dfs(i,j,val):
            if 0<=i<n and 0<=j<m and grid[i][j]==1:
                grid[i][j]=val
                dfs(i-1,j,val)
                dfs(i+1,j,val)
                dfs(i,j-1,val)
                dfs(i,j+1,val)
        for i in range(n):
            for j in range(m):
                if (i==0 or j==0 or i==n-1 or j==m-1) and grid[i][j]==1:
                    dfs(i,j,0)
        print(grid)
        return sum(sum(row) for row in grid)