class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        m , n = len(grid) , len(grid[0])
        l , r , cnt = 0, m-1, 0
        while l < n and r >= 0:
            if grid[r][l] < 0:
                cnt += n-l
                r -= 1
            else:
                l += 1
        return cnt