class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        m1,m2=prices[0],float('-inf')
        for i in range(len(prices)):
            m1=min(m1,prices[i])
            m2=max(m2,prices[i]-m1)
        return m2