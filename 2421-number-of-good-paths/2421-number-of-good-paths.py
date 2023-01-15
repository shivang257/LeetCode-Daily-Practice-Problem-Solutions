class Solution:
    def numberOfGoodPaths(self, vals: List[int], edges: List[List[int]]) -> int:
        res = n = len(vals)
        f = list(range(n))
        count = [Counter({vals[i]: 1}) for i in range(n)]
        edges = sorted([max(vals[i], vals[j]),i,j] for i,j in edges)

        def find(x):
            if f[x] != x:
                f[x] = find(f[x])
            return f[x]

        for v,i,j in edges:
            fi, fj = find(i), find(j)
            cj, ci = count[fi][v], count[fj][v]
            res += ci * cj
            f[fj] = fi
            count[fi] = Counter({v: ci + cj})
        return res