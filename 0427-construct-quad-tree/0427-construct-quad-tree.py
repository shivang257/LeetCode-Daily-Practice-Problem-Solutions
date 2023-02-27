class Solution:
    def construct(self, grid):

        def helper(grid, row, col, length):
            if length == 1:
                return Node(grid[row][col] == 1, True, None, None, None, None)

            topLeft = helper(grid, row, col, length // 2)
            topRight = helper(grid, row, col + length // 2, length // 2)
            bottomLeft = helper(grid, row + length // 2, col, length // 2)
            bottomRight = helper(grid, row + length // 2, col + length // 2, length // 2)

            if topLeft.isLeaf == topRight.isLeaf == bottomLeft.isLeaf == bottomRight.isLeaf == True:
                if topLeft.val == topRight.val == bottomLeft.val == bottomRight.val:
                    return Node(topLeft.val, True, None, None, None, None)

            return Node("*", False, topLeft, topRight, bottomLeft, bottomRight)

        return helper(grid, 0, 0, len(grid))