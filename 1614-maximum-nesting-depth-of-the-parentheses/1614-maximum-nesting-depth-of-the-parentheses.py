class Solution:
    def maxDepth(self, s: str) -> int:
        res=0
        curr=0
        for i in s:
            if i=='(':
                curr+=1
                res=max(curr,res)
            if i==')':
                curr-=1
        return res