class Solution:
    def canJump(self, nums: List[int]) -> bool:
        goal=0
        for i in range(len(nums))[::-1]:
            if i+nums[i]>=goal:
                goal=i
        return goal==0