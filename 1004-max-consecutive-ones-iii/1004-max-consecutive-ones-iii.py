class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        left,right=0,0
        res=0
        zero=0
        while right<len(nums):
            zero+=1-nums[right]
            right+=1
            if zero>k:
                zero-=1-nums[left]
                left+=1
            res=max(res,right-left)
        return res