class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res=[]
        def dfs(nums,path,total):
            if total==target:
                res.append(path)
                return
            if total>target:
                return
            for i in range(len(nums)):
                dfs(nums[i:],path+[nums[i]],total+nums[i])
        dfs(candidates,[],0)
        return res