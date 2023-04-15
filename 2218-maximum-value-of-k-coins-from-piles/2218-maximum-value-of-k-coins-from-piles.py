class Solution:
    def maxValueOfCoins(self, A, K):
        
        @functools.lru_cache(None)
        def dp(i, k):
            if k == 0 or i == len(A): return 0
            res, cur = dp(i + 1, k), 0
            for j in range(min(len(A[i]), k)):
                cur += A[i][j]
                res = max(res, cur + dp(i+1, k-j-1))
            return res
        
        return dp(0, K)