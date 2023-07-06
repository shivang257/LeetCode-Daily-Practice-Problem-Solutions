class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        j,res=0,len(nums)+1
        for i in range(len(nums)):
            target-=nums[i]
            while target<=0:
                res=min(i-j+1,res)
                target+=nums[j]
                j+=1
        return res%(len(nums)+1)