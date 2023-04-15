class Solution:
    def miceAndCheese(self, A: List[int], B: List[int], k: int) -> int:
        return sum(B) + sum(nlargest(k, (a - b for a, b in zip(A, B))))