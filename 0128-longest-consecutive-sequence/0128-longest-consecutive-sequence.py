class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        arr=set(nums)
        c=0
        for i in arr:
            if i-1 not in arr:
                t=0
                while i+t in arr:
                    t+=1
                c=max(t,c)
        return c