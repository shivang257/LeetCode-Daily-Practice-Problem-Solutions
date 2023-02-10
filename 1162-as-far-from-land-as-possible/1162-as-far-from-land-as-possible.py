class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        n, res = len(grid), 0
        land = {(i, j) for i, j in product(range(n), range(n)) if grid[i][j]}
        water = {(i, j) for i, j in product(range(n), range(n)) if not grid[i][j]}
        while water:
            if not land: return -1
            land = {(x, y) for i, j in land for x, y in ((i+1, j), (i-1, j), (i, j+1), (i, j-1)) if (x, y) in water}
            water -= land
            res += 1
        return res or -1