class Solution:
    def decodeAtIndex(self, S, K):
        N = 0
        for i, c in enumerate(S):
            N = N * int(c) if c.isdigit() else N + 1
            if K <= N: break
        for j in range(i, -1, -1):
            c = S[j]
            if c.isdigit():
                N /= int(c)
                K %= N
            else:
                if K == N or K == 0: return c
                N -= 1