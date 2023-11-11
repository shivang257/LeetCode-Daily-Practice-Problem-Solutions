class Graph:
        
    def __init__(self, n: int, edges: List[List[int]]):
        self.adj_list = [[] for _ in range(n)]
        for a, b, cost in edges:
            self.adj_list[a].append((b, cost))

    def addEdge(self, edge: List[int]) -> None:
        a, b, cost = edge
        self.adj_list[a].append((b, cost))

    def shortestPath(self, node1: int, node2: int) -> int:
        n, pq = len(self.adj_list), [(0, node1)]
        dist = [inf] * (n)
        dist[node1] = 0

        while pq:
            d, node = heappop(pq)
            if node == node2: return d
            if d > dist[node]: continue
            for neighbor, cost in self.adj_list[node]:
                new_dist = d + cost
                if new_dist < dist[neighbor]:
                    dist[neighbor] = new_dist
                    heappush(pq, (new_dist, neighbor))
        return -1
