class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        res = set()

        def BT(i,subsequence):
            nonlocal res
            if len(subsequence)>1:
                res.add(tuple(subsequence))
            if i==len(nums):
                return
            
            if not subsequence or nums[i] >= subsequence[-1]:
                BT(i+1, subsequence+[nums[i]]) 
            BT(i+1, subsequence)
        
        BT(0,[])
        return res