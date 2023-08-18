import collections
class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        connected = collections.defaultdict(set)
        for a, b in roads:
            connected[a].add(b)
            connected[b].add(a)
        M = 0
        for i in range(n):
            for j in range(i + 1, n):
                M = max(M, len(connected[i]) + len(connected[j]) - (i in connected[j]))
        return M