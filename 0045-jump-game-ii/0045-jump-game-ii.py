class Solution:
    def jump(self, nums: List[int]) -> int:
        # the initial range (after 0th jump) is [0,0]
        l = r = 0
        nJumps = 0
        while r < len(nums) - 1:
            nJumps += 1
            furthest = max([i + nums[i] for i in range(l,r+1)])
            l,r = r+1, furthest

        return nJumps