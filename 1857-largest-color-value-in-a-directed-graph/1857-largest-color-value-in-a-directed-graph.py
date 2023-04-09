class Solution:
    def largestPathValue(self, colors, edges):
        n, k = len(colors), 26
        indegrees = [0] * n
        graph = [[] for _ in range(n)]
        for u, v in edges:
            graph[u].append(v)
            indegrees[v] += 1
        zero_indegree = set(i for i in range(n) if indegrees[i] == 0)
        counts = [[0] * k for _ in range(n)]
        for i, c in enumerate(colors):
            counts[i][ord(c) - ord('a')] += 1
        max_count, visited = 0, 0
        while zero_indegree:
            u = zero_indegree.pop()
            visited += 1
            for v in graph[u]:
                for i in range(k):
                    counts[v][i] = max(counts[v][i], counts[u][i] + (ord(colors[v]) - ord('a') == i))
                indegrees[v] -= 1
                if indegrees[v] == 0:
                    zero_indegree.add(v)
            max_count = max(max_count, max(counts[u]))
        return max_count if visited == n else -1