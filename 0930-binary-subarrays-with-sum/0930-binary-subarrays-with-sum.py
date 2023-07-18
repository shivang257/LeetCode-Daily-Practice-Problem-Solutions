class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        def atmost(nums,k):
            if k<0:
                return 0
            l,s,res=0,0,0
            for r in range(len(nums)):
                s+=nums[r]
                while s>k:
                    s-=nums[l]
                    l+=1
                res+=r-l+1
            return res
        return atmost(nums,goal)-atmost(nums,goal-1)