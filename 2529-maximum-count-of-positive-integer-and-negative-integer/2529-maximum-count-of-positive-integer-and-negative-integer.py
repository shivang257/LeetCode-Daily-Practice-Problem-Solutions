class Solution:
    def binarySearch(self,nums,target):
        left,right=0,len(nums)-1
        while left<=right:
            mid=(left+right)//2
            if nums[mid]<target:
                left=mid+1
            else:
                right=mid-1
        return left
    def maximumCount(self, nums: List[int]) -> int:
        return max(self.binarySearch(nums,0),len(nums)-self.binarySearch(nums,1))