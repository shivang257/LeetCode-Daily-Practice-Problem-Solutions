class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        m1=prices[0]
        b1=float("-inf")
        for i in range(len(prices)):
            m1=min(m1,prices[i])
            b1=max(prices[i]-m1,b1)
        return b1