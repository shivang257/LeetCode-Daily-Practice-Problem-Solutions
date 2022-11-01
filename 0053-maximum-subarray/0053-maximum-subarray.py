class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        m1=nums[0]
        m2=nums[0]
        for i in range(1,len(nums)):
            m1=max(nums[i],m1+nums[i])
            m2=max(m2,m1)
        return m2