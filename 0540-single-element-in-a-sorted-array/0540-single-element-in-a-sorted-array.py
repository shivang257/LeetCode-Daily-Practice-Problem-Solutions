class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        left,right=0,len(nums)-1
        while left<right:
            mid=(left+right)//2
            if (mid%2==1 and nums[mid-1]==nums[mid]) or (mid%2==0 and nums[mid]==nums[mid+1]):
                left=mid+1
            else:
                right=mid
        return nums[left]