class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        l=[]
        for i in range(len(nums)):
            if nums[i]==target:
                l.append(i)
        if not l:
            return [-1,-1]
        if len(l)==1:
            return [l[0],l[0]]
        return [min(l),max(l)]