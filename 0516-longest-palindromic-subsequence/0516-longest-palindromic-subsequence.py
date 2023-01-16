class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        a=s[::-1]
        n=len(s)
        d=[[0]*(n+1) for i in range(n+1)]
        for i in range(1,n+1):
            for j in range(1,n+1):
                if s[i-1]==a[j-1]:
                    d[i][j]=1+d[i-1][j-1]
                else:
                    d[i][j]=max(d[i-1][j],d[i][j-1])
        return d[-1][-1]