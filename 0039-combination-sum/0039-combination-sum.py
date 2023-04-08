class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res=[]
        def dfs(nums,path,target,res):
            if target<0:
                return
            if target==0:
                res.append(path)
                return
            for i in range(len(nums)):
                dfs(nums[i:],path+[nums[i]],target-nums[i],res)
        dfs(candidates,[],target,res)
        return res