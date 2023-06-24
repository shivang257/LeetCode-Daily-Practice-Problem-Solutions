class Solution:
    def longestString(self, x: int, y: int, z: int) -> int:
        return min(x + y + z, x + x + 1 + z, y + y + 1 + z) * 2