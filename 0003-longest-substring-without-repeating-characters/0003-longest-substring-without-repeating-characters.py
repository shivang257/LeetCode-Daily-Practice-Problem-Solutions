class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        seen = {}
        output = 0
        
        for right, curr in enumerate(s):
            if curr in seen:
                left = max(left, seen[curr] + 1)
            output = max(output, right - left + 1)
            seen[curr] = right

        return output