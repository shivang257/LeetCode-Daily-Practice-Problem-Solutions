class Solution:
    def dfs(self,s,path,res):
        if not s:
            res.append(path)
            return
        for i in range(1,len(s)+1):
            if self.isPal(s[:i]):
                self.dfs(s[i:],path+[s[:i]],res)
    def isPal(self,s):
        return s==s[::-1]
    
    def partition(self, s: str) -> List[List[str]]:
        if not s:
            return [[]]
        res=[]
        self.dfs(s,[],res)
        return res