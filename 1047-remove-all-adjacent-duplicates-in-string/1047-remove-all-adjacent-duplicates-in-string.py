class Solution:
    def removeDuplicates(self, s: str) -> str:
        res=[]
        for c in s:
            res.pop() if res and res[-1]==c else res.append(c)
        return "".join(res)
    
