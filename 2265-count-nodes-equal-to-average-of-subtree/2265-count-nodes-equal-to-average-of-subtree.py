class Solution:
    def averageOfSubtree(self, root: Optional[TreeNode]) -> int:
        def is_target(current_value, left_sum, left_total, right_sum, right_total):
            subtree_average = (left_sum + current_value + right_sum) // (left_total + right_total + 1)
            is_target = subtree_average == current_value
            return is_target
            

        def helper(node):
            if not node:
                return 0,0,0
            left_sum, left_total, left_result = helper(node.left)
            right_sum, right_total, right_result = helper(node.right)
            is_current_target = is_target(node.val, left_sum, left_total, right_sum, right_total)
            
            current_sum = left_sum + right_sum + node.val
            current_total = left_total + right_total + 1
            current_result = left_result + right_result + is_current_target
            return current_sum, current_total, current_result
        result = helper(root)
        return result[2]