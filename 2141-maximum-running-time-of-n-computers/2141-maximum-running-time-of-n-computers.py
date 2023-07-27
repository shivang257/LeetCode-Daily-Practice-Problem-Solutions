class Solution:
    def maxRunTime(self, n: int, batteries: List[int]) -> int:
        batteries.sort()
        su = sum(batteries)
        while batteries[-1] > su // n:
            n -= 1
            su -= batteries.pop()
        return su // n