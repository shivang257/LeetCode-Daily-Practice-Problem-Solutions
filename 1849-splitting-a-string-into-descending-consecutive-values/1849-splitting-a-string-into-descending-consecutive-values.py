class Solution:
    def dfs(self,index,prev,s):
        if index==len(s):
            return True
        for i in range(index,len(s)):
            val=int(s[index:i+1])
            if val+1==prev and self.dfs(i+1,val,s):
                return True
        return False
    def splitString(self, s: str) -> bool:
        for i in range(len(s)-1):
            val=int(s[:i+1])
            if self.dfs(i+1,val,s):
                return True
        return False