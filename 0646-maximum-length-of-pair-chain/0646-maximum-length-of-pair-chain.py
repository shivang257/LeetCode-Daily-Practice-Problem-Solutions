class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        cur,res=float('-inf'),0
        for p in sorted(pairs,key=lambda x:x[1]):
            if cur<p[0]:
                cur=p[1]
                res+=1
        return res