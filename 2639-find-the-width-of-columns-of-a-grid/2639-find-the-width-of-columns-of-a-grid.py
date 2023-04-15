class Solution:
    def findColumnWidth(self, grid: List[List[int]]) -> List[int]:
        l=[]
        for i in range(len(grid[0])):
            m=0
            for j in range(len(grid)):
                s=str(grid[j][i])
                m=max(m,len(s))
            l.append(m)
        return l