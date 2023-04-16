class Solution:
    def maxDivScore(self, nums: List[int], divisors: List[int]) -> int:
        l=[0]*len(divisors)
        divisors.sort()
        for i in range(len(divisors)):
            m=0
            for j in range(len(nums)):
                if nums[j]%divisors[i]==0:
                    l[i]+=1
        if l.count(0)==len(l):
            return min(divisors)
        return divisors[l.index(max(l))]