class Solution(object):
    def minOperations(self, A):
        count = Counter(A).values()
        return -1 if 1 in count else sum((c + 2) // 3 for c in count)