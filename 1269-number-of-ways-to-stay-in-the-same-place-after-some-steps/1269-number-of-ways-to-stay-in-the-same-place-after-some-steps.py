class Solution:
    def numWays(self, steps, n, mod=10 ** 9 + 7):
        A = [0, 1]
        for t in range(steps):
            A[1:] = [sum(A[i - 1:i + 2]) % mod for i in range(1, min(n + 1, t + 3))]
        return A[1] % mod