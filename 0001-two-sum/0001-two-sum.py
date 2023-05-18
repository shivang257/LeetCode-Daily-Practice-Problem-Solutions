class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen={}
        
        for i,j in enumerate(nums):
            a=target-j
            if a in seen:
                return [seen[a],i]
            seen[j]=i