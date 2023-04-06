class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        n,m=len(grid),len(grid[0])
        
        def dfs(i,j,val):
            if 0<=i<n and 0<=j<m and grid[i][j]==0:
                grid[i][j]=val
                dfs(i-1,j,val)
                dfs(i,j+1,val)
                dfs(i+1,j,val)
                dfs(i,j-1,val)
        for i in range(n):
            for j in range(m):
                if (i==0 or j==0 or i==n-1 or j==m-1) and grid[i][j]==0:
                    dfs(i,j,1)
        ans=0
        for i in range(n):
            for j in range(m):
                if grid[i][j]==0:
                    dfs(i,j,1)
                    ans+=1
        return ans