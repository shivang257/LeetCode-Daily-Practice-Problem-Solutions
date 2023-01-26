"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        OldToNew={}
        
        def clone(node):
            if node in OldToNew:
                return OldToNew[node]
            copy=Node(node.val)
            OldToNew[node]=copy
            for n in node.neighbors:
                copy.neighbors.append(clone(n))
            return copy
        return clone(node) if node else None