class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        res=[[1]]
        for i in range(1,rowIndex+1):
            t1,t2=[0]+res[-1],res[-1]+[0]
            res.append([t1[i]+t2[i] for i in range(len(t1))])
        return res[rowIndex]