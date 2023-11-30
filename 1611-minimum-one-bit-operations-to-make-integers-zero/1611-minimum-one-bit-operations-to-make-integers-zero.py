class Solution:
    dp = {0: 0}
    def minimumOneBitOperations(self, n):
        if n not in self.dp:
            b = 1
            while (b << 1) <= n:
                b = b << 1
            self.dp[n] = self.minimumOneBitOperations((b >> 1) ^ b ^ n) + 1 + b - 1
        return self.dp[n]