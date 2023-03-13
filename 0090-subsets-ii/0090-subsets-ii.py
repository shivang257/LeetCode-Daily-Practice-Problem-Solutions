class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        ans=[[]]
        nums.sort()
        for i in nums:
            ans+=[[i]+j for j in ans]
        l=[]
        for i in ans:
            if i not in l:
                l.append(i)
        return l