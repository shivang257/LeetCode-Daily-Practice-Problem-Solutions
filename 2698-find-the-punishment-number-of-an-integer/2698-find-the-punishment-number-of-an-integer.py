class Solution:
    def check(self, idx, p, target):
        if idx == len(p):
            return target == 0
        if target < 0:
            return False
        for i in range(idx, len(p)):
            x = p[idx:i + 1]
            y = int(x)
            if self.check(i + 1, p, target - y):
                return True
        return False

    def punishmentNumber(self, n):
        ans = 0
        for i in range(1, n + 1):
            x = i * i
            p = str(x)
            if self.check(0, p, i):
                ans += (i * i)
        return ans