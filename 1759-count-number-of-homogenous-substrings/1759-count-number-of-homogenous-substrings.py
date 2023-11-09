class Solution:
    def countHomogenous(self, s: str) -> int:
        res = 0
        for c, s in groupby(s):
            n = len(list(s))
            res += n * (n + 1) // 2
        return res % (10**9 + 7)
    
    