class Solution:
    def findGCD(self, nums: List[int]) -> int:
        return math.gcd(max(nums),min(nums))