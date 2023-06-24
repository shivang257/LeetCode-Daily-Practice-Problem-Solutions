class Solution(object):
    def tallestBillboard(self, rods):
        dp = {0: 0}
        for x in rods:
            for d, y in dp.items():
                dp[d + x] = max(dp.get(x + d, 0), y)
                dp[abs(d - x)] = max(dp.get(abs(d - x), 0), y + min(d, x))
        return dp[0]