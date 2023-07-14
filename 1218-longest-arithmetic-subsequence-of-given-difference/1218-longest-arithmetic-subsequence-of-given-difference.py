class Solution:
    def longestSubsequence(self, arr: List[int], diff: int) -> int:
        res={}
        for num in arr:
            res[num] = res.get(num-diff, 0) + 1
        return max(res.values())