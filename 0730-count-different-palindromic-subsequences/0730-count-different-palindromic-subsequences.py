class Solution:
    def countPalindromicSubsequences(self, s: str) -> int:
        md = 10**9+7
        n = len(s)
        dp = [[0] * n for _ in range(n)]
        
        for i in range(n):
            dp[i][i] = 1
            
        for d in range(1,n):
            for beg in range(n-d):
                end = beg + d
                
                if s[beg] == s[end]:
                    dp[beg][end] = 2 * dp[beg + 1][end - 1]
                
                    l, r = beg + 1, end - 1
                    while l <= r and s[beg] != s[l]:
                        l += 1
                    while l <= r and s[beg] != s[r]:
                        r -= 1
                    
                    if l > r:
                        dp[beg][end] += 2
                    elif l == r:
                        dp[beg][end] += 1
                    else:
                        dp[beg][end] -= dp[l + 1][r - 1]
                else:
                    dp[beg][end] = dp[beg + 1][end] + dp[beg][end - 1] - dp[beg + 1][end - 1]
                    
                dp[beg][end] %= md
                
        return dp[0][-1]