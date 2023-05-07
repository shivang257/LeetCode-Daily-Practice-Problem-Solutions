class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        pathSum=float('-inf')
        
        def dfs(node):
            nonlocal pathSum
            
            if not node:
                return 0
            
            leftSum= max(dfs(node.left),0)
            rightSum=max(dfs(node.right),0)
            
            current=node.val+leftSum+rightSum
            
            pathSum=max(pathSum,current)
            
            return node.val+max(leftSum,rightSum)
        dfs(root)
        return pathSum