class Solution:
    def partitionString(self, s: str) -> int:
        l,ans=[],1
        for i in s:
            if i in l:
                l=[i]
                ans+=1
            else:
                l+=[i]
        return ans