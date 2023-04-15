from collections import Counter
class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        count = Counter(nums)
        k = max(count.values())
        nums.sort()
        return [nums[i::k] for i in range(k)]