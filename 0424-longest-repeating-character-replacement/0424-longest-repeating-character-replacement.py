class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        maxf,res=0,0
        j=0
        count=Counter()
        for i in range(len(s)):
            count[s[i]]+=1
            maxf=max(maxf,count[s[i]])
            if i-j+1 - maxf > k:
                count[s[j]]-=1
                j+=1
            res=max(res,i-j+1)
        return res