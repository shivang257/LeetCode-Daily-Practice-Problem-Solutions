class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        inc,dec=1,1
        n=len(nums)
        for i in range(1,n):
            if nums[i]<nums[i-1]:
                dec=inc+1
            elif nums[i]>nums[i-1]:
                inc=dec+1
        return max(dec,inc)