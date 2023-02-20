class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        a=prices[0]
        b=0
        for i in range(1,len(prices)):
            a=min(a,prices[i])
            b=max(prices[i]-a,b)
        return b