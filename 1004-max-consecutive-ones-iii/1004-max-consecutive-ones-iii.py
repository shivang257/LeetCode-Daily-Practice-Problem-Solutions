class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        right,left,zero=0,0,0
        ans=0
        while right<len(nums):
            if nums[right]==0:
                zero+=1
            right+=1
            if zero>k:
                zero-=1-nums[left]
                left+=1
            ans=max(ans,right-left)
        return ans