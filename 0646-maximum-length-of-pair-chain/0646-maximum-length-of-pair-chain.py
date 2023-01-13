class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        pairs=sorted(pairs,key=lambda x:x[1])
        n=len(pairs)
        dp=[1]*(n)
        for i in range(n):
            for j in range(i):
                if pairs[i][0]>pairs[j][1] and dp[i]<dp[j]+1:
                    dp[i]=dp[j]+1
        return max(dp)