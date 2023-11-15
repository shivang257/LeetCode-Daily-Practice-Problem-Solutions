class Solution:
    def maximumElementAfterDecrementingAndRearranging(self, A: List[int]) -> int:
        A.sort()
        pre = 0
        for a in A:
            pre = min(pre + 1, a)
        return pre