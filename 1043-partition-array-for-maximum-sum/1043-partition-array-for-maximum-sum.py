class Solution:
        def maxSumAfterPartitioning(self, A, K):
            N = len(A)
            dp = [0] * K
            for i in range(1, N + 1):
                best = curMax = 0
                for k in range(1, min(K, i) + 1):
                    curMax = max(curMax, A[i - k])
                    best = max(best, dp[(i - k) % K] + curMax * k)
                dp[i % K] = best
            return dp[N % K]