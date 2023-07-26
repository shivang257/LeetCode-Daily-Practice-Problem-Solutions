class Solution:
    def minSpeedOnTime(self, dist: List[int], hour: float) -> int:
        lo, hi, n = 1, 10 ** 7 + 1, len(dist)
        while lo < hi:
            speed = lo + (hi - lo) // 2
            need = dist[-1] / speed + sum((dist[i] + speed - 1) // speed for i in range(n - 1))
            if need > hour:
                lo = speed + 1
            else:
                hi = speed
        return -1 if lo == 10 ** 7 + 1 else lo