class Solution:
    def minimumRounds(self, tasks):
        freq = Counter(tasks).values()
        return -1 if 1 in freq else sum((a + 2) // 3 for a in freq)