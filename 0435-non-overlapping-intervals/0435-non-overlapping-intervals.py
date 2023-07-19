class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda i:i[1])
        out=[]
        ans=0
        for i,j in intervals:
            if out and (i<out[-1][1]):
                ans+=1
            else:
                out.append([i,j])
        return ans