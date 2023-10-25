class Solution:
    def kthGrammar(self, N, K):
        return bin(K - 1).count('1') & 1