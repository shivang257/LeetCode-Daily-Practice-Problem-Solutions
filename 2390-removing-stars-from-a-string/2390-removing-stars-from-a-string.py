class Solution:
    def removeStars(self, s):
        res = []
        for c in s:
            if c != '*':
                res += c
            elif res:
                res.pop()
        return ''.join(res)