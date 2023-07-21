class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        res=0
        zero=0
        left=0
        for right in range(len(nums)):
            if nums[right]==0:
                zero+=1
            while zero>k:
                zero-=1-nums[left]
                left+=1
            res=max(res,right-left+1)
        return res