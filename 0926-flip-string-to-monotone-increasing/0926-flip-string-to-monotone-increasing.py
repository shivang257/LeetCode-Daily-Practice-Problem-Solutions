class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        dp=[0]*(len(s)+1)
        n=(len(s))
        ones=0
        for i in range(1,n+1):
            if s[i-1]=='1':
                dp[i]=dp[i-1]
                ones+=1
            else:
                dp[i]=min(dp[i-1]+1,ones)
        return dp[-1]