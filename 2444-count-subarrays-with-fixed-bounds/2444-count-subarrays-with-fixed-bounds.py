class Solution:
    def countSubarrays(self, A: List[int], minK: int, maxK: int) -> int:
        res,jmin,jmax,jbad = 0,-1,-1,-1
        for i,a in enumerate(A):
            if not minK <= a <= maxK: jbad = i
            if a == minK: jmin = i
            if a == maxK: jmax = i
            res += max(0, min(jmin, jmax) - jbad)
        return res
