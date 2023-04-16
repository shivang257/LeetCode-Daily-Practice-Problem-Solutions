class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res=[]
        nums.sort()
        def backtrack(i,path):
            if path not in res:
                res.append(path)
            for j in range(i,len(nums)):
                backtrack(j+1,path+[nums[j]])
        backtrack(0,[])
        return res