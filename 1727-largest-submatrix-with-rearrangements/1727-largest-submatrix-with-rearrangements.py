class Solution:
    def largestSubmatrix(self, A: List[List[int]]) -> int:
        m, n = len(A), len(A[0])
        H = [0] * n
        ans = 0
        for i in range(m):
            for j in range(n):
                H[j] = H[j] + 1 if A[i][j] else 0
            ans = max(ans, self.getMaxArea(H[:]))
        return ans

    def getMaxArea(self, heights):
        heights.sort()
        area = 0
        n = len(heights)
        for i in range(n):
            h = heights[i]
            area = max(area, h * (n - i))
        return area