class Solution:
    def closestMeetingNode(self, edges: List[int], node1: int, node2: int) -> int:
        INF = float('inf')
        N = len(edges)
        dist_node1 = [INF for _ in range(N)]
        dist_node2 = [INF for _ in range(N)]
        
        def dfs(node, di, d):
            if d[node] > di: 
                d[node] = di
                if edges[node] != -1:
                    dfs(edges[node], di+1, d)
        
        dfs(node1, 0, dist_node1)
        dfs(node2, 0, dist_node2)

        for i in range(N):
            dist_node1[i] = max(dist_node1[i], dist_node2[i])
                        
        ans = dist_node1.index(min(dist_node1))
        return ans if dist_node1[ans] != INF else -1