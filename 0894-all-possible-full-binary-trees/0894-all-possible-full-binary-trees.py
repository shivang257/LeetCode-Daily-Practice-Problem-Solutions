class Solution:
    def allPossibleFBT(self, N: int) -> List[Optional[TreeNode]]:
        N -= 1
        if N == 0: return [TreeNode(0)]
        ret = []
        for l in range(1, min(20, N), 2):
            for left in self.allPossibleFBT(l):
                for right in self.allPossibleFBT(N - l):
                    root = TreeNode(0)
                    root.left = left
                    root.right = right
                    ret += [root]
        return ret