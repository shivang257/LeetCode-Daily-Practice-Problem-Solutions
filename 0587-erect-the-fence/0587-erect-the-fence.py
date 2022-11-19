class Solution:
    def outerTrees(self, points: List[List[int]]) -> List[List[int]]:
        
        def crossProduct(p1,p2,p3):
            ### V1 = (a,b), V2 = (c,d)
            ### V1 X V2 = a*d - b*c
            a = p2[0]-p1[0]
            b = p2[1]-p1[1]
            c = p3[0]-p1[0]
            d = p3[1]-p1[1]
            return a*d - b*c
        
        def constructHalfHull(points):
            stack = []
            for p in points:
                ### if the chain formed by the current point
                ### and the last two points in the stack is not counterclockwise, pop it
                while len(stack)>=2 and crossProduct(stack[-2],stack[-1],p)>0:
                    stack.pop()
                ### append the current point.
                stack.append(tuple(p))
            return stack
        
        ### sort points by x, so we are moving from left to right
        points.sort()
        leftToRight = constructHalfHull(points)
        ### reverse points, so we are moving from right to left
        rightToLeft = constructHalfHull(points[::-1])
        
        ### it is posible that the top and bottom parts have same points (e.g., all points form a line)
        ### we remove the duplicated points using a set
        return list(set(leftToRight + rightToLeft))