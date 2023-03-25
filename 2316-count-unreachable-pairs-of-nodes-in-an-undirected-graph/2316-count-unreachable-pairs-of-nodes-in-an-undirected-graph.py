class UnionFind:
    def __init__(self, size):
        self.root = [i for i in range(size)]
        self.rank = [1] * size
        
    def find(self, node):
        if node != self.root[node]:
            self.root[node] = self.find(self.root[node])
        return self.root[node]
    
    def union(self, node1, node2):
        root1 = self.find(node1)
        root2 = self.find(node2)
        if root1 != root2:
            if self.rank[root1] > self.rank[root2]:
                self.root[root2] = root1
            elif self.rank[root1] < self.rank[root2]:
                self.root[root1] = root2
            else:
                self.root[root2] = root1
                self.rank[root1] += 1
                
class Solution:
    def countPairs(self, n: int, edges: List[List[int]]) -> int:
        uf = UnionFind(n)
        for node1, node2 in edges:
            uf.union(node1 - 1, node2 - 1)
        group_sizes = list(Counter([uf.find(i) for i in range(n)]).values())
        ans = 0
        first_group_size = group_sizes[0]
        for i in range(1, len(group_sizes)):
            ans += first_group_size * group_sizes[i]
            first_group_size += group_sizes[i]  
        return ans
