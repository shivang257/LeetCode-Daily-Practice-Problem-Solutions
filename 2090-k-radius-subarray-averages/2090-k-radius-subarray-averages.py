class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        ans=[-1]*(len(nums))
        left,diameter,currSum=0,2*k+1,0
        for right in range(len(nums)):
            currSum+=nums[right]
            if right-left+1>=diameter:
                ans[left+k]=currSum//diameter
                currSum-=nums[left]
                left+=1
        return ans