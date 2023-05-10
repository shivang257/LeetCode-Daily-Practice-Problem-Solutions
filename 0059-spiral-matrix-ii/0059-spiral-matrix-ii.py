class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        A, lo = [], n*n+1
        while lo > 1:
            lo, hi = lo - len(A), lo
            b=zip(*A[::-1])
            A = [range(lo, hi)] + list(zip(*A[::-1]))
        return A