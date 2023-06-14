class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def binary(nums,target,leftbias):
            left,right=0,len(nums)-1
            i=-1
            while left<=right:
                mid=(left+right)//2
                if nums[mid]<target:
                    left=mid+1
                elif nums[mid]>target:
                    right=mid-1
                else:
                    i=mid
                    if leftbias:
                        right=mid-1
                    else:
                        left=mid+1
            return i
        left=binary(nums,target,True)
        right=binary(nums,target,False)
        return [left,right]