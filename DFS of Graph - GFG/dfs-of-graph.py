#User function Template for python3

class Solution:
    def dfs(self,v,i,adj,visited,result):
        visited[i]=True
        result.append(i)
        for j in adj[i]:
            if not visited[j]:
                self.dfs(v,j,adj,visited,result)
    #Function to return a list containing the DFS traversal of the graph.
    def dfsOfGraph(self, V, adj):
        result=[]
        visited=[False]*V
        self.dfs(V,0,adj,visited,result)
        return result


#{ 
 # Driver Code Starts
if __name__ == '__main__':
    T=int(input())
    while T>0:
        V,E=map(int,input().split())
        adj=[[] for i in range(V+1)]
        for i in range(E):
            u,v=map(int,input().split())
            adj[u].append(v)
            adj[v].append(u)
        ob=Solution()
        ans=ob.dfsOfGraph(V,adj)
        for i in range(len(ans)):
            print(ans[i],end=" ")
        print()
        T-=1
# } Driver Code Ends