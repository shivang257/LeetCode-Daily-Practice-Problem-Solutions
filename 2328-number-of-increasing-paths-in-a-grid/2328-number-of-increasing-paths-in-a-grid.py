class Solution:
    def countPaths(self, A: List[List[int]]) -> int:
        m, n, mod = len(A), len(A[0]), 10 ** 9 + 7

        @lru_cache(None)
        def count(i, j):
            res = 1
            for x, y in [[i, j + 1], [i, j - 1], [i + 1, j], [i - 1, j]]:
                if 0 <= x < m and 0 <= y < n and A[x][y] < A[i][j]:
                    res += count(x, y) % mod
            return res

        return sum(count(i,j) for i in range(m) for j in range(n)) % mod