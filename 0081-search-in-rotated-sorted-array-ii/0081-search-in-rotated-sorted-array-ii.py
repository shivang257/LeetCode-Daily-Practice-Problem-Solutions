class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        nums.sort()
        left,right=0,len(nums)-1
        while left<=right:
            mid=(left+right)//2
            if nums[mid]==target:
                return True
            elif nums[mid]>target:
                right=mid-1
            else:
                left=mid+1
        return False