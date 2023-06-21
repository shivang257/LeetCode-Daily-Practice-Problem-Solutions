class Solution:
    def minCost(self, A, cost):
        def f(x):
            return sum(abs(a - x) * c for a,c in zip(A, cost))

        l, r = min(A), max(A)
        res = f(l)
        while l < r:
            x = (l + r) // 2
            y1, y2 = f(x), f(x + 1)
            res = min(y1, y2)
            if y1 < y2:
                r = x
            else:
                l = x + 1
        return res