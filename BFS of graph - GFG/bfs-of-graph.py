class Solution:
    def bfsOfGraph(self, V, adj):
        queue=[]
        queue.append(0)
        res,visited=[],[False]*V
        while queue:
            a=queue.pop(0)
            res.append(a)
            
            for i in adj[a]:
                if not visited[i]:
                    queue.append(i)
                visited[i]=True
        return res
            


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