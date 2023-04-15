class Solution:
    def findTheLongestBalancedSubstring(self, s: str) -> int:
        res,temp=0,'01'
        while temp in s:
            temp='0'+temp+'1'
            res=max(res,len(temp)-2)
        return res