class Solution:
    def countRoutes(self, l: List[int], start: int, fin: int, fuel: int) -> int:
        @lru_cache(None)
        def dfs(i: int, f: int) -> int:
            return 0 if f < 0 else (1 if i == fin else 0) + sum(0 if i == j else dfs(j, f - abs(l[j] - l[i])) for j in range(len(l)))
        return dfs(start, fuel) % 1000000007