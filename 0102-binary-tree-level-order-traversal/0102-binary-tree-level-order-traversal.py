# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return
        queue=deque()
        queue.append(root)
        ans=[]
        while queue:
            temp=[]
            size=len(queue)
            for i in range(size):
                n=queue.popleft()
                if n.left:
                    queue.append(n.left)
                if n.right:
                    queue.append(n.right)
                temp.append(n.val)
            ans.append(temp)
        return (ans)