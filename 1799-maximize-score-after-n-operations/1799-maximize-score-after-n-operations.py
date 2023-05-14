class Solution:
    def maxScore(self, n: List[int]) -> int:
        @lru_cache(None)
        def dfs(i: int, mask: int) -> int:
            if i > len(n) // 2:
                return 0;
            res = 0
            for j in range(len(n)):
                for k in range(j + 1, len(n)):
                    new_mask = (1 << j) + (1 << k)
                    if not mask & new_mask:
                        res = max(res, i * gcd(n[j], n[k]) + dfs(i + 1, mask + new_mask))
            return res
        return dfs(1, 0)