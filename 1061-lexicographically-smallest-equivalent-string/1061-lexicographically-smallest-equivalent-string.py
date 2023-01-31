class DisjointSet:
    def __init__(self, n):
        self.parent = [i for i in range(n+1)]
        self.size = [1 for _ in range(n+1)]

    def findPar(self, node):
        if node == self.parent[node]:
            return node
        self.parent[node] = self.findPar(self.parent[node])
        return self.parent[node]

    def unionBySize(self, u, v):
        up = self.findPar(u)
        uv = self.findPar(v)
        if up == uv:
            return
        if up < uv:
            self.parent[uv] = up
        else:
            self.parent[up] = uv

class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        n = len(s1)
        ds = DisjointSet(26)
        for i in range(n):
            ds.unionBySize(ord(s1[i]) - ord('a'), ord(s2[i]) - ord('a'))
        res = ""
        for i in range(len(baseStr)):
            res += chr(ds.findPar(ord(baseStr[i]) - ord('a')) + ord('a'))
        return res