class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        zero=0
        left,right,ans=0,0,0
        while right<len(nums):
            zero+=1-nums[right]
            right+=1
            if zero>1:
                zero-=1-nums[left]
                left+=1
            ans=max(ans,right-left-1)
        return ans