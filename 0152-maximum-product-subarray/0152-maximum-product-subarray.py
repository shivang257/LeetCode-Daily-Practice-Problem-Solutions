class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        a=nums[::-1]
        for i in range(1,len(nums)):
            a[i]*=a[i-1] or 1
            nums[i]*=nums[i-1] or 1
        return max(a+nums)