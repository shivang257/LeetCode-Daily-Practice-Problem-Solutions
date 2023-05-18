class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen={}
        
        for i,j in enumerate(nums):
            seen[j]=i
        for i,j in enumerate(nums):
            a=target-j
            if a in seen and seen[a]!=i:
                return [seen[a],i]