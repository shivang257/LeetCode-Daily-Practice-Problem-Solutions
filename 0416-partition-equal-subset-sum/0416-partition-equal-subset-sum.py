class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        n=len(nums)
        if sum(nums)%2!=0:
            return False
        a=sum(nums)//2
        dp=[[False]*(a+1) for i in range(n+1)]
        dp[0][0]=True
        for i in range(1,n+1):
            for j in range(1,a+1):
                if j>=nums[i-1]:
                    dp[i][j]=dp[i-1][j] or dp[i-1][j-nums[i-1]]
                else:
                    dp[i][j]=dp[i-1][j]
        return dp[-1][-1]