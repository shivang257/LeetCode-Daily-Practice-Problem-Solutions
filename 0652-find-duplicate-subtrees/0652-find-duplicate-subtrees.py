class Solution(object):
    def findDuplicateSubtrees(self, root):
        # Concept - We can use a hashmap to store the all the trees and their roots
        # Also advantage of using hashmap is you can easily find for the repeated
        # or duplicate trees
        hashmap = {}
        res = []
        self.solve(root, hashmap)

        # Once the hashmap is built, we can just travserse through the values 
        # and find out the values that are greater than 1 are repeated
        for val, node in hashmap.values():
            if val > 1:
                res.append(node)
        return res
    
    def solve(self, root, hashmap):
        if not root:
            return 'X'
        
        a = self.solve(root.left, hashmap)
        b = self.solve(root.right, hashmap)
        
        # Pre-order tree representation for storing the tree
        temp = str(root.val) + ' ' + a + ' ' + b
        
        # Check if it is already in hashmap
        if temp not in hashmap:
            hashmap[temp] = [1, root]
        
        else:
            hashmap[temp][0] += 1
            
        return temp