class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n=len(nums)
        nums.sort()
        if nums[n-1]!=n:
            return n
        for i in range(n):
            if nums[i]!=i:
                return i