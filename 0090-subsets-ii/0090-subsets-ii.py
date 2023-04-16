class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res=[]
        nums.sort()
        def backtrack(nums,path):
            res.append(path)
            for j in range(len(nums)):
                if j>0 and nums[j]==nums[j-1]:
                    continue
                backtrack(nums[j+1:],path+[nums[j]])
        backtrack(nums,[])
        return res