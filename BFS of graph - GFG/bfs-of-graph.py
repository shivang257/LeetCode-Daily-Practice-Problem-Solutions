#User function Template for python3

class Solution:
    #Function to return Breadth First Traversal of given graph.
    def bfsOfGraph(self, V, adj):
        queue=[]
        result=[]
        visited=[False]*V
        
        queue.append(0)
        visited[0]=True
        
        while queue:
            a=queue.pop(0)
            result.append(a)
            
            for i in adj[a]:
                if visited[i]==False:
                    queue.append(i)
                    visited[i]=True
        return result
            
#{ 
 # Driver Code Starts

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		V, E = map(int, input().split())
		adj = [[] for i in range(V)]
		for _ in range(E):
			u, v = map(int, input().split())
			adj[u].append(v)
		ob = Solution()
		ans = ob.bfsOfGraph(V, adj)
		for i in range(len(ans)):
		    print(ans[i], end = " ")
		print()
        

# } Driver Code Ends