class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        ans = 0
        seen = []
        for x in nums: 
            k = bisect_right(seen, 2*x)
            ans += len(seen) - k
            insort(seen, x)
        return ans 