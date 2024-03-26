class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        nums = list(set(nums))    
        nums = [x for x in nums if x > 0]    
        nums.sort()
        if 1 not in nums: return 1
        for i in range(len(nums)):
            if i == len(nums) - 1: return nums[i] + 1
            if nums[i] + 1 != nums[i+1]:
                return nums[i] + 1