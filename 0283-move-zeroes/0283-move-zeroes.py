class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        left,right=0,0
        while right<len(nums):
            if nums[right]!=0 and nums[left]==0:
                nums[left],nums[right]=nums[right],nums[left]
            if nums[left]!=0:
                left+=1
            right+=1
        return nums