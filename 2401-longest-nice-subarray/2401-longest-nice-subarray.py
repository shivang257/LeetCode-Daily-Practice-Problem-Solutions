class Solution:
    def longestNiceSubarray(self, nums: List[int]) -> int:
        res,a,i=0,0,0
        for j in range(len(nums)):
            while a &nums[j]:
                a^=nums[i]
                i+=1
            a|=nums[j]
            res=max(res,j-i+1)
        return res