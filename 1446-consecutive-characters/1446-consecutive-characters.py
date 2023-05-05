class Solution:
    def maxPower(self, s: str) -> int:
        if not s:
            return s
        c=1
        ans=1
        for i in range(1,len(s)):
            if s[i-1]==s[i]:
                c+=1
                ans=max(c,ans)
            else:
                c=1
        return ans