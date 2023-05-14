class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        nums.sort()
        i=0
        for j in range(len(nums)):
            k+=nums[j]
            if k < nums[j]*(j-i+1):
                k-=nums[i]
                i+=1
        return j-i+1