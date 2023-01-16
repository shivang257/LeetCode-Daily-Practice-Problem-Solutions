class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        intervals.append(newInterval)
        intervals.sort()
        out=[intervals[0]]
        for i in range(1,len(intervals)):
            last=out[-1][1]
            if intervals[i][0]<=last:
                out[-1][1]=max(last,intervals[i][1])
            else:
                out.append(intervals[i])
        return out