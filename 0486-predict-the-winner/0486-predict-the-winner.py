class Solution:
    def PredictTheWinner(self, nums: List[int]) -> bool:
        dp={}
        #DP MEMOIZATION
        def find(i,j):
            if i==j:
                return nums[i]
            if (i,j) not in dp:
                dp[i,j]=max(nums[i]-find(i+1,j), nums[j]-find(i,j-1))
            return dp[i,j]
        return find(0,len(nums)-1)>=0