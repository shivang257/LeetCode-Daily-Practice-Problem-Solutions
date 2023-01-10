class Solution:
    def minDistance(self, s: str, t: str) -> int:
        dp=[[0]*(len(t)+1) for i in range(len(s)+1)]
        n=len(t)
        sn=len(s)
        for i in range(sn+1):
            for j in range(n+1):
                if i==0:
                    dp[i][j]=j
                if j==0:
                    dp[i][j]=i
        for i in range(sn):
            for j in range(n):
                if s[i]==t[j]:
                    dp[i+1][j+1]=dp[i][j]
                else:
                    dp[i+1][j+1]=1+min(dp[i][j],dp[i+1][j],dp[i][j+1])
        return dp[-1][-1]