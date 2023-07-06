class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left,res=0,0
        seen={}
        for right,curr in enumerate(s):
            if curr in seen:
                left=max(left,seen[curr]+1)
            res=max(right-left+1,res)
            seen[curr]=right
        return res