import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        h=[-i for i in stones]
        heapq.heapify(h)
        while len(h)>1 and h[0]!=0:
            heapq.heappush(h,heapq.heappop(h)-heapq.heappop(h))
        return -h[0]