class Solution:
    def dfs(self,node,c,seen):
        for nei,adj in enumerate(c[node]):
            if adj and nei not in seen:
                seen.add(nei)
                self.dfs(nei,c,seen)
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        seen=set()
        n=len(isConnected)
        res=0
        for i in range(n):
            if i not in seen:
                res+=1
                self.dfs(i,isConnected,seen)
        return res