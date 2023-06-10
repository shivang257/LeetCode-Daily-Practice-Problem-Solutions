class Solution:
    def longestSemiRepetitiveSubstring(self, s: str) -> int:
        res=0
        tab=[1]
        for i in range(1,len(s)):
            if ( s[i]==s[i-1]):
                tab.append(1)
            else:
                tab[-1]=tab[-1]+1
        for j in range(1,len(tab)):
            res=max(res,tab[j]+tab[j-1])
        
        return max(res,tab[0])