class Solution:
    def firstCompleteIndex(self, arr, mat):
        m, n = len(mat), len(mat[0])
        loc = {x : (i, j) for i, row in enumerate(mat) for j, x in enumerate(row)}
        rows = [0]*m
        cols = [0]*n
        for k, x in enumerate(arr): 
            i, j = loc[x]
            rows[i] += 1
            cols[j] += 1
            if rows[i] == n or cols[j] == m: return k 