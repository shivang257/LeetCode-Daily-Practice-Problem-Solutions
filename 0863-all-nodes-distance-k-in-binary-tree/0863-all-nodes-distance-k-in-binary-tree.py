from collections import defaultdict

class Solution:
    
    def __init__(self):
        self.graph = defaultdict(set)
        self.visited = set()
        
    
    def distanceK(self, root, target, K):
        self.dfs(root, target.val)
        res = [target.val]
        
        for _ in range(K):
            size, level = len(res), []
            
            for _ in range(size):
                cur = res.pop()
                if cur not in self.visited:
                    level += self.graph.get(cur, [])
                    self.visited.add(cur)
            
            res = level
            
        return [val for val in res if val not in self.visited]
            
    
    def dfs(self, root: TreeNode, target: int) -> None:
        if not root:
            return
        
        if root.left:
            self.graph[root.val].add(root.left.val)
            self.graph[root.left.val].add(root.val)
            self.dfs(root.left, target)
            
        if root.right:
            self.graph[root.val].add(root.right.val)
            self.graph[root.right.val].add(root.val)
            self.dfs(root.right, target)