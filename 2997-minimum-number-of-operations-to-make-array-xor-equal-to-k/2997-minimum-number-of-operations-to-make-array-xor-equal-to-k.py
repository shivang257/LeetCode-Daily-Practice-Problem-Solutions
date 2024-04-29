class Solution:
    def minOperations(self, A: List[int], k: int) -> int:
        return reduce(xor, A, k).bit_count()