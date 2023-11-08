class Solution:
    def isReachableAtTime(self, sx: int, sy: int, fx: int, fy: int, t: int) -> bool:
        need = max(abs(sx - fx), abs(sy - fy))
        return t >= need if need else t != 1