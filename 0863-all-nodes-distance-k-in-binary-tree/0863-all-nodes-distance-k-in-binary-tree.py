class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        adjacent=defaultdict(list)
        
        def dfs(node,parent_node):
            if parent_node:
                adjacent[node].append(parent_node)
            if node.left:
                adjacent[node].append(node.left)
                dfs(node.left,node)
            if node.right:
                adjacent[node].append(node.right)
                dfs(node.right,node)
        dfs(root,None)
        seen={target}
        ans=[]
        def bfs(node,k):
            if k==0:
                ans.append(node.val)
            else:
                seen.add(node)
                for adj in adjacent[node]:
                    if adj not in seen:
                        bfs(adj,k-1)
        bfs(target,k)
        return ans