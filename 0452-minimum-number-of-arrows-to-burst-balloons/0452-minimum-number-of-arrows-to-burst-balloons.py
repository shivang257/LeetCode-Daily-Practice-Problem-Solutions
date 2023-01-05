class Solution(object):
    def findMinArrowShots(self, points):
        points=sorted(points,key=lambda x:x[1])
        res,end=0,-float(math.inf)
        for i in points:
            if i[0]>end:
                res+=1
                end=i[1]
        return res