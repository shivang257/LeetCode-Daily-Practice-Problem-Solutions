class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        v='aeiou'
        ans,c=0,0
        for i in range(len(s)):
            if i>=k and s[i-k] in v:
                c-=1
            if s[i] in v:
                c+=1
            ans=max(c,ans)
        return ans