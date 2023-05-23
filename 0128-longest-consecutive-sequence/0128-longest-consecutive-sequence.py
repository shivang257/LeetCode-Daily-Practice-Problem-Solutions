class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        l=set(nums)
        c=0
        for i in nums:
            if i-1 not in l:
                t=0 
                while i+t in l:
                    t+=1
                c=max(c,t)
        return c