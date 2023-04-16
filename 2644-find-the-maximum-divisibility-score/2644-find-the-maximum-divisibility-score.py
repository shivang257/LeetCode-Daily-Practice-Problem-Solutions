class Solution:
    def maxDivScore(self, nums: List[int], divisors: List[int]) -> int:
        ans=-1
        most=-1
        for d in divisors:
            cnt=sum(1 for n in nums if n%d==0)
            if cnt>most or cnt==most and d<ans:
                ans=d
                most=cnt

        return ans 