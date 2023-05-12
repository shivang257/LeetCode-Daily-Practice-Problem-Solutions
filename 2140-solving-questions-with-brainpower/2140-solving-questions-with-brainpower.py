class Solution:
    def mostPoints(self, Q: List[List[int]]) -> int:
        @cache
        def dp(i):
            if i >= len(Q): return 0
            points, jump = Q[i][0], Q[i][1]
            return max(dp(i + 1), points + dp(i + jump + 1))
        return dp(0)
            