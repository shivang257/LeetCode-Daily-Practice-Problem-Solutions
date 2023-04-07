class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        n=len(nums)
        lo,hi=0,len(nums)-1
        while lo<hi:
            mid= 2*((lo+hi)//4)
            if nums[mid]==nums[mid+1]:
                lo=mid+2
            else:
                hi=mid
        return nums[lo]