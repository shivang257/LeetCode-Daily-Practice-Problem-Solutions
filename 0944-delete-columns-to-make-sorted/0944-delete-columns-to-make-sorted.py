class Solution:
    def minDeletionSize(self, A: List[str]) -> int:
        return sum(list(col) != sorted(col) for col in zip(*A))