class Solution:
    def putMarbles(self, weights: List[int], k: int) -> int:
        n=len(weights)-1
        res=[0]*n
        for i in range(len(res)):
            res[i]=weights[i]+weights[i+1]
        res.sort()
        ans=0
        for i in range(k-1):
            ans+=res[n-1-i]-res[i]
        return ans