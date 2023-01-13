#User function Template for python3

class Solution:
    def maxSquare(self, n, m, matrix):
        res=0
        dp=[[0]*(m+1) for i in range(n+1)]
        for i in range(n):
            for j in range(m):
                if matrix[i][j]==1:
                    dp[i+1][j+1]=min(dp[i][j],dp[i][j+1],dp[i+1][j])+1
                res=max(res,dp[i+1][j+1])
        return res


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n, m = [int(x) for x in input().split()]
        mat = [[0]*m for x in range(n)]
        arr = input().split()
        for i in range(n*m):
            mat[i//m][i%m] = int(arr[i])
        
        ob = Solution()
        print(ob.maxSquare(n, m, mat))
# } Driver Code Ends