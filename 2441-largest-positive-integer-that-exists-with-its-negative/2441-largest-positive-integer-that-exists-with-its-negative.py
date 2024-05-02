class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        l=[]
        for i in nums:
            if -1*i in nums:
                l.append(abs(i))
        return max(l) if l else -1
        