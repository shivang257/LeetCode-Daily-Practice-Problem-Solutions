class Solution:
    def removeStones(self, points):
        uf = {}
        def find(x):
            if x != uf.setdefault(x, x):
                uf[x] = find(uf[x])
            return uf[x]
        for i, j in points:
            uf[find(i)] = find(~j)
        return len(points) - len({find(x) for x in uf})