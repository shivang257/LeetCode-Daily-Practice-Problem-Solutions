class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        mx=1
        i=0
        while i<len(nums):
            curr=1
            while i+1<len(nums) and nums[i]<nums[i+1]:
                curr+=1
                i+=1
            mx=max(mx,curr)
            i+=1
        return mx