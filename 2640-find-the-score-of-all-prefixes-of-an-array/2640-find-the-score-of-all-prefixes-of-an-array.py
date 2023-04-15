class Solution:
    def findPrefixScore(self, nums: List[int]) -> List[int]:
        l,s,m=[],0,0
        for i in range(len(nums)):
            m=max(m,nums[i])
            s+=nums[i]+m
            l.append(s)
        return l