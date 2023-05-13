class Solution:
    def sumOfPower(self, nums: List[int]) -> int:
        mod, pre, res = 10 ** 9 + 7, 0, 0
        for x in sorted(nums):
            res = (res + x * x * x + x * x * pre) % mod 
            pre = (pre * 2 + x) % mod
        return res