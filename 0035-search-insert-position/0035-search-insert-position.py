class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if not nums:
            return 0
        for i,n in enumerate(nums):
            if n>=target:
                return i
        return len(nums)