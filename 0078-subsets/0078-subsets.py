class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res=[]
        n=len(nums)
        def backtrack(i,path):
            res.append(path)    
            for j in range(i,len(nums)):
                backtrack(j+1,path+[nums[j]])
        backtrack(0,[])
        return res