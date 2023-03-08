class Solution:
    def minEatingSpeed(self, piles, H):
        l, r = 1, max(piles)
        while l < r:
            m = (l + r) // 2
            if sum((p + m - 1) // m for p in piles) > H:
                l = m + 1
            else:
                r = m
        return l