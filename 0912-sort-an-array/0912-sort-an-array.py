class Solution:
    def sortArray(self, N: List[int]) -> List[int]:
        L = len(N)
        for i in range(1,L): bisect.insort_left(N, N.pop(i), 0, i)
        return N