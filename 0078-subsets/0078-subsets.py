class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res=[]
        n=len(nums)
        def backtrack(i,nums,path):
            res.append(path)    
            for i in range(len(nums)):
                backtrack(i+1,nums[i+1:],path+[nums[i]])
        backtrack(0,nums,[])
        return res