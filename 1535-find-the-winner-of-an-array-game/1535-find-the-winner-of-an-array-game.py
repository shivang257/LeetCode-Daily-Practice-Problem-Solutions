class Solution:
    def getWinner(self, A, k):
        cur = A[0]
        win = 0
        for i in range(1, len(A)):
            if A[i] > cur:
                cur = A[i]
                win = 0
            win += 1
            if (win == k): break
        return cur