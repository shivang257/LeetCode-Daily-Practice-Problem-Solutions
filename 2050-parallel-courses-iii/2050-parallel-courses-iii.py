class Solution:
    def minimumTime(self, n, R, T):
        G = defaultdict(list)
        for x, y in R:
            G[y].append(x)

        @lru_cache(None)
        def dp(node):
            return T[node - 1] + max([dp(child) for child in G[node]] + [0])

        return max(dp(i) for i in range(1, n+1))