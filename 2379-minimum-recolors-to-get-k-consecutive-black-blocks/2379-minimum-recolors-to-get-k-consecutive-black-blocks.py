class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        ans,c=blocks[:k].count('W'),blocks[:k].count("W")
        s='W'
        for i in range(len(blocks)):
            if i>=k and blocks[i-k]==s:
                c-=1
            if i>=k and blocks[i]==s:
                c+=1
            ans=min(c,ans)
        return ans