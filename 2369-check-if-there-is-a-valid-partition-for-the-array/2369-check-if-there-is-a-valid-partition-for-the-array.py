class Solution:
    def validPartition(self, nums: List[int]) -> bool:
        n = len(nums) 
        if n == 1: 
            return False 
        dp = [True, False, nums[0] == nums[1] if n > 1 else False] 
        for i in range(2, n): 
            current_dp = False
            if nums[i] == nums[i-1] and dp[1]: 
                current_dp = True
            elif nums[i] == nums[i-1] == nums[i-2] and dp[0]: 
                current_dp = True 
            elif nums[i] - nums[i-1] == 1 and nums[i-1] - nums[i-2] == 1 and dp[0]: 
                current_dp = True 
            dp[0], dp[1], dp[2] = dp[1], dp[2], current_dp 
        return dp[2]