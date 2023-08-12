class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m, n = len(obstacleGrid), len(obstacleGrid[0])

        dp = [ [0]*n for _ in range(m) ]
        
        for i in range(m):
            for j in range(n):
                if obstacleGrid[i][j] == 0:
                    if i==j==0: # dp[0][0]=1
                        dp[i][j] = 1
                        continue
                    else:         
                        dp[i][j] = dp[i-1][j] + dp[i][j-1]
                
        return dp[m-1][n-1] 