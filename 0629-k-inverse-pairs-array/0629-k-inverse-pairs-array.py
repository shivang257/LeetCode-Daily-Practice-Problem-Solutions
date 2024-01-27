class Solution:
    def kInversePairs(self, N, K):
        MOD = 10**9 + 7
        ds = [0] + [1] * (K + 1)
        for n in range(2, N+1):
            new = [0]
            for k in range(K+1):
                v = ds[k+1]
                v -= ds[k-n+1] if k >= n else 0
                new.append( (new[-1] + v) % MOD )
            ds = new
        return (ds[K+1] - ds[K]) % MOD