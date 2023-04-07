class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        n=len(nums)
        lo,hi=0,len(nums)-1
        while lo<hi:
            mid=(lo+hi)//2
            if mid%2==0 and nums[mid]==nums[mid+1] or mid%2!=0 and nums[mid]==nums[mid-1]:
                lo=mid+1
            else:
                hi=mid
        return nums[lo]