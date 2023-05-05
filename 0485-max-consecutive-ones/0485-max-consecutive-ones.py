class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        ans,c=0,0
        for num in nums:
            if num==1:
                c+=1
                ans=max(ans,c)
            else:
                c=0
        return ans