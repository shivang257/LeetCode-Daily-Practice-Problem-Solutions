class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        res=0
        n=len(matrix)
        m=len(matrix[0])
        dp=[[0]*(m+1) for i in range(n+1)]
        for i in range(n):
            for j in range(m):
                if matrix[i][j]=='1':
                    dp[i+1][j+1]=min(dp[i][j],dp[i][j+1],dp[i+1][j])+1
                res=max(res,dp[i+1][j+1])
        return res*res