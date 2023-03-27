class Solution:
    def collectTheCoins(self, coins: List[int], edges: List[List[int]]) -> int:
        n = len(coins)
        tree = [set() for _ in range(n)]
        for u, v in edges: 
            tree[u].add(v)
            tree[v].add(u)
        leaf = deque()
        for u in range(n):
            while len(tree[u]) == 1 and not coins[u]: 
                v = tree[u].pop()
                tree[v].remove(u)
                u = v 
            if len(tree[u]) == 1: leaf.append(u)
        for _ in range(2): 
            for _ in range(len(leaf)): 
                u = leaf.popleft()
                if tree[u]: 
                    v = tree[u].pop()
                    tree[v].remove(u)
                    if len(tree[v]) == 1: leaf.append(v)
        return sum(len(tree[u]) for u in range(n))