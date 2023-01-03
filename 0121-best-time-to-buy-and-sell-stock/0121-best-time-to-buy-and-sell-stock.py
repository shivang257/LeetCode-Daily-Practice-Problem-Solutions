class Solution:
    def maxProfit(self, p: List[int]) -> int:
        a,b=p[0],0
        for i in range(len(p)):
            a=min(p[i],a)
            b=max(b,p[i]-a)
        return b