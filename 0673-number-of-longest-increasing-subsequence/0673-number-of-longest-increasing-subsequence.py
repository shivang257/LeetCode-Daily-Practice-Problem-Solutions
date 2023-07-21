class Solution:
    def findNumberOfLIS(self, nums):
        if not nums: return 0
        n = len(nums) + 1
    
        decks, ends_decks, paths = [[] for _ in range(n)], [float("inf")]*n, [[0] for _ in range(n)]
        for num in nums:
            idx = bisect.bisect_left(ends_decks, num)
            n_paths = 1
            if idx > 0:
                l = bisect.bisect(decks[idx-1], -num)
                n_paths = paths[idx-1][-1] - paths[idx-1][l]
            
            decks[idx].append(-num)
            ends_decks[idx] = num
            paths[idx].append(n_paths + paths[idx][-1])
                
        return paths[paths.index([0]) - 1][-1]