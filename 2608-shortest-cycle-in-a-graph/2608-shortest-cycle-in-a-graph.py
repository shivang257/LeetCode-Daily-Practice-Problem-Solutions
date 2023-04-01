class Solution:
    def findShortestCycle(self, n: int, edges: List[List[int]]) -> int:
        G = [[] for _ in range(n)]
        for i, j in edges:
            G[i].append(j)
            G[j].append(i)
        def root(i):
            dis = [inf] * n
            dis[i] = 0
            bfs = [i]
            for i in bfs:
                for j in G[i]:
                    if dis[j] == inf:
                        dis[j] = 1 + dis[i]
                        bfs.append(j)
                    elif dis[i] <= dis[j]:
                        return dis[i] + dis[j] + 1
            return inf
        res = min(map(root, range(n)))
        return res if res < inf else -1