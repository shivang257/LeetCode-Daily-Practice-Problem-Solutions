class Solution:
    def minimumTime(self, time: List[int], totalTrips: int) -> int:
        return bisect_left(range(1, 10**14), totalTrips, key= lambda x: sum(x // t for t in time)) + 1