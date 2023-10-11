class Solution:
    def fullBloomFlowers(self, A: List[List[int]], persons: List[int]) -> List[int]:
        start, end = sorted(a for a,b in A), sorted(b for a,b in A)
        return [bisect_right(start, t) - bisect_left(end, t) for t in persons]