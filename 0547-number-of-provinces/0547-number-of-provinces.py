class Solution:
    def dfs(self,node,c,visited):
        for nei,adj in enumerate(c[node]):
            if adj and not visited[nei]:
                visited[nei]=True
                self.dfs(nei,c,visited)
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        visited=[False]*(len(isConnected))
        n=len(isConnected)
        res=0
        for i in range(n):
            if not visited[i]:
                res+=1
                self.dfs(i,isConnected,visited)
        return res