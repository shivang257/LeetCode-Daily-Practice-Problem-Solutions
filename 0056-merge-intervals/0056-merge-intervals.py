class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        output=[intervals[0]]
        for start,end in intervals[1:]:
            last=output[-1][1]
            if start<=last:
                output[-1][1]=max(last,end)
            else:
                output.append([start,end])
        return output