class Solution:
    def checkValidString(self, s):
            cmin = cmax = 0
            for i in s:
                if i == '(':
                    cmax += 1
                    cmin += 1
                if i == ')':
                    cmax -= 1
                    cmin = max(cmin - 1, 0)
                if i == '*':
                    cmax += 1
                    cmin = max(cmin - 1, 0)
                if cmax < 0:
                    return False
            return cmin == 0