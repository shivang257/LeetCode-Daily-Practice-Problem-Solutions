from heapq import heappush, heappop
from math import log2

class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start: int, end: int) -> float:
        adj = [set() for _ in range(n)]
        for (u, v), p in zip(edges, succProb):
            adj[u].add((v, log2(1/p)))
            adj[v].add((u, log2(1/p)))
        dist = [float('inf') for _ in range(n)]
        dist[start] = 0
        h = [(0, start)]
        while h:
            d, u = heappop(h)
            if d == dist[u]:
                for (v, p) in adj[u]:
                    if dist[u] + p < dist[v]:
                        dist[v] = dist[u] + p
                        heappush(h, (dist[v], v))
        return 1 / (2 ** dist[end])