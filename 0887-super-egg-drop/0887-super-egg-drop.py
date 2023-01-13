class Solution(object):
    def superEggDrop(self, K, N):
        """
        :type K: int
        :type N: int
        :rtype: int
        """ 
        dp = range(N+1)
        for i in range(2, K+1):
            k = 1
            ndp = [0, 1] + [float('inf')]*(N-1)
            for j in range(2, N+1):
                while k < j+1 and ndp[j-k] > dp[k-1]:
                    k += 1
                ndp[j] = 1 + dp[k-1]
            dp = ndp
        return dp[N]