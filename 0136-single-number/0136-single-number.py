class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        a=Counter(nums).most_common()
        return a[len(a)-1][0]