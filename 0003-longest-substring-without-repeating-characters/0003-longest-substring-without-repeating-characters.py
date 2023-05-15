class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        count=set()
        res=0
        l=0
        for r in range(len(s)):
            while s[r] in count:
                count.remove(s[l])
                l+=1
            count.add(s[r])
            res=max(res,r-l+1)
        return res