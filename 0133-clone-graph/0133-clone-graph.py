class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        OldToNew = {}
        
        def clone(node):
            if node in OldToNew:
                return OldToNew[node]
            copy=Node(node.val)
            OldToNew[node]=copy
            for nei in node.neighbors:
                copy.neighbors.append(clone(nei))
            return copy
        return clone(node) if node else None
    