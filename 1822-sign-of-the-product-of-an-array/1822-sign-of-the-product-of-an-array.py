class Solution:
    def arraySign(self, nums: List[int]) -> int:
        ans = 1
        for x in nums: 
            if x == 0: return 0 
            if x < 0: ans *= -1
        return ans 