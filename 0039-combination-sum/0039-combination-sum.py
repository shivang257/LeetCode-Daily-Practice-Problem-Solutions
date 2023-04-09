class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res=[]
        def dfs(nums,path,target):
            if target==0:
                res.append(path)
                return
            if target<0:
                return 
            for i in range(len(nums)):
                dfs(nums[i:],path+[nums[i]],target-nums[i])
        dfs(candidates,[],target)
        return res