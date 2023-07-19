class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        l=0
        res=0
        count={c:0 for c in 'abc'}
        for r in range(len(s)):
            count[s[r]]+=1
            while count['a'] and count['b'] and count['c']:
                count[s[l]]-=1
                l+=1
            res+=l
        return res