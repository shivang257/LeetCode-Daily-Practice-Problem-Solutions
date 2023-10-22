class Solution:
    def maximumScore(self, A, k):
        res = mini = A[k]
        i, j, n = k, k, len(A)
        while i > 0 or j < n - 1:
            if (A[i - 1] if i else 0) < (A[j + 1] if j < n - 1 else 0):
                j += 1
            else:
                i -= 1
            mini = min(mini, A[i], A[j])
            res = max(res, mini * (j - i + 1))
        return res