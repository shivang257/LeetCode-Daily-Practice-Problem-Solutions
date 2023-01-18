class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        curmax,curmin,mas,mis=0,0,nums[0],nums[0]
        for i in nums:
            curmax=max(curmax+i,i)
            mas=max(mas,curmax)
            curmin=min(curmin+i,i)
            mis=min(mis,curmin)
        return max(mas,sum(nums)-mis) if mas>0 else mas