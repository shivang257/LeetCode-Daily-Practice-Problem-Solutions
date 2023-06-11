class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        mi,mx=min(strs),max(strs)
        for i in range(len(mi)):
            if mi[i]!=mx[i]:
                return mi[:i]
        return mi