class UnionFindSet:
    def __init__(self, n=0):
        self.parents = {}
        self.ranks = {}
        self.count = 0
        for i in range(n):
            self.add(i)

    def add(self, p):
        self.parents[p] = p
        self.ranks[p] = 1
        self.count += 1

    def find(self, u):
        if u != self.parents[u]:
            self.parents[u] = self.find(self.parents[u])
        return self.parents[u]

    def union(self, u, v):
        pu, pv = self.find(u), self.find(v)
        if pu == pv: 
            return False
        if self.ranks[pu] < self.ranks[pv]:
            self.parents[pu] = pv
        elif self.ranks[pu] > self.ranks[pv]:
            self.parents[pv] = pu
        else:        
            self.parents[pv] = pu
            self.ranks[pu] += 1
        self.count -= 1
        return True
    
# UnionFind + Kruskal + Enumerate edges
# O(ElogE + E^2 + E^2)
class Solution:
    def findCriticalAndPseudoCriticalEdges(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        # sort edges in asc order based on weight
        edges = [(u, v, w, i) for i, (u, v, w) in enumerate(edges)]
        edges.sort(key=lambda x: x[2])
        
        # do not use this edge
        def find_mst_without_this_edge(edge_idx):
            union_find_set = UnionFindSet(n)
            ans = 0
            for i, (u, v, w, _) in enumerate(edges):
                # do not use this edge
                if i == edge_idx:
                    continue
                if union_find_set.union(u, v):
                    ans += w
            parent = union_find_set.find(0)
            return ans if all(union_find_set.find(i) == parent for i in range(n)) else inf
        
        # need to use this edge
        def find_mst_with_this_edge(edge_idx):
            union_find_set = UnionFindSet(n)
            # use this edge first
            u0, v0, w0, _ = edges[edge_idx]
            ans = w0
            union_find_set.union(u0, v0)
            for i, (u, v, w, _) in enumerate(edges):
                # do not use this edge
                if i == edge_idx:
                    continue
                if union_find_set.union(u, v):
                    ans += w
            parent = union_find_set.find(0)
            return ans if all(union_find_set.find(i) == parent for i in range(n)) else inf
        
        # normal MST total weight
        base = find_mst_without_this_edge(-1)
        cri, p_cri = set(), set()
        for i in range(len(edges)):
            wgt_excl = find_mst_without_this_edge(i)
            # if not included, MST total weight would increase
            if wgt_excl > base:
                cri.add(edges[i][3])
            else:
                wgt_incl = find_mst_with_this_edge(i)
                # with this edge, MST total weight doesn't change
                if wgt_incl == base:
                    p_cri.add(edges[i][3])
    
        return [cri, p_cri]