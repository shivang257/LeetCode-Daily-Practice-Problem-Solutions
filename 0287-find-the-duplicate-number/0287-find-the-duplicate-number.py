class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        a=Counter(nums).most_common()
        return (a[0][0])