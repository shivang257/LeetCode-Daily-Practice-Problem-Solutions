class Solution:
    def longestArithSeqLength(self, nums: List[int]) -> int:
        dp={}
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                dp[j,nums[j]-nums[i]]=dp.get((i,nums[j]-nums[i]),1)+1
        return max(dp.values())